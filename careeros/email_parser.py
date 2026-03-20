"""
Email ingestion for CareerOS.
Accepts raw email text pasted by user. Parses it to:
  - Identify which contact it relates to (or suggests creating a new one)
  - Classify as sent / received
  - Extract date and key information
  - Return a structured dict the caller uses to update DB
"""

import re
from datetime import date, datetime
from models import Contact

# ── Date extraction ───────────────────────────────────────────────────────────

DATE_PATTERNS = [
    r'\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})\b',
    r'\b((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4})\b',
    r'\b(\d{4}[-/]\d{2}[-/]\d{2})\b',
    r'\b(\d{1,2}/\d{1,2}/\d{4})\b',
    r'\bOn\s+((?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s+\d{1,2}\s+\w+\s+\d{4})',
    r'\bDate:\s*(.+?)(?:\n|$)',
]

DATE_FORMATS = [
    "%d %B %Y", "%d %b %Y", "%B %d %Y", "%B %d, %Y",
    "%b %d %Y", "%b %d, %Y", "%Y-%m-%d", "%Y/%m/%d",
    "%m/%d/%Y", "%d/%m/%Y",
    "%a, %d %b %Y", "%A, %d %B %Y",
]


def _extract_date(text):
    for pat in DATE_PATTERNS:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            raw = m.group(1).strip().rstrip(',')
            for fmt in DATE_FORMATS:
                try:
                    return datetime.strptime(raw, fmt).date()
                except ValueError:
                    pass
    return date.today()


# ── Direction detection ───────────────────────────────────────────────────────

SENT_SIGNALS = [
    r'\bFrom:.*?@.*?\b',     # From: me@...
    r'\bI wrote\b', r'\bI sent\b', r'\bI emailed\b',
    r'\bDear\s+\w', r'\bHi\s+\w', r'\bHello\s+\w',
    r'\bBest regards\b', r'\bKind regards\b', r'\bThanks,\b', r'\bThank you,\b',
    r'\bLooking forward\b',
]

RECEIVED_SIGNALS = [
    r'\bFrom:.*?(?:worldbank|irena|google|ifc|imf|wri|e3|amazon|avina)\b',
    r'\bThank you for reaching out\b', r'\bThank you for your\b',
    r'\bWe would like to\b', r'\bPlease find\b',
    r'\bI am pleased\b', r'\bI wanted to follow up\b',
]


def _classify_direction(text):
    sent_score = sum(1 for p in SENT_SIGNALS if re.search(p, text, re.IGNORECASE))
    recv_score = sum(1 for p in RECEIVED_SIGNALS if re.search(p, text, re.IGNORECASE))

    # Look for "From: me" vs "From: them" heuristic
    from_match = re.search(r'From:\s*(.+)', text, re.IGNORECASE)
    if from_match:
        from_val = from_match.group(1).lower()
        if any(x in from_val for x in ['harvard', 'hks', 'me', 'myself']):
            return 'sent'

    if recv_score > sent_score:
        return 'received'
    return 'sent'


# ── Contact matching ──────────────────────────────────────────────────────────

def _match_contact(text):
    """
    Return (contact, confidence) where confidence is 'high'/'medium'/'none'.
    Tries:
      1. Email address match
      2. Full name exact match
      3. Partial name / org keyword match
    """
    contacts = Contact.query.all()

    # 1. Email match
    emails_found = re.findall(r'[\w.+-]+@[\w-]+\.\w+', text)
    for c in contacts:
        if c.email and c.email.lower() in [e.lower() for e in emails_found]:
            return c, 'high'

    # 2. Exact name match (case-insensitive)
    for c in contacts:
        if re.search(r'\b' + re.escape(c.name) + r'\b', text, re.IGNORECASE):
            return c, 'high'

    # 3. First name + org keyword
    for c in contacts:
        first = c.name.split()[0]
        org_words = [w for w in (c.organization or '').split() if len(w) > 3]
        name_hit = re.search(r'\b' + re.escape(first) + r'\b', text, re.IGNORECASE)
        org_hit  = any(re.search(r'\b' + re.escape(w) + r'\b', text, re.IGNORECASE) for w in org_words)
        if name_hit and org_hit:
            return c, 'medium'

    # 4. First name only
    for c in contacts:
        first = c.name.split()[0]
        if len(first) > 3 and re.search(r'\b' + re.escape(first) + r'\b', text, re.IGNORECASE):
            return c, 'medium'

    return None, 'none'


# ── Key info extraction ───────────────────────────────────────────────────────

def _extract_key_info(text):
    """Pull out meeting proposals, job references, commitments."""
    snippets = []

    patterns = [
        (r'(?:call|meeting|chat|connect|schedule|speak).{0,80}', 'Meeting/call reference'),
        (r'(?:role|position|opportunity|opening|vacancy).{0,80}', 'Role/opportunity'),
        (r'(?:interview|next step|follow.?up).{0,80}', 'Next step'),
        (r'(?:attached|please find|sharing|sending).{0,80}', 'Attachment/material'),
        (r'(?:happy to|glad to|would love to).{0,80}', 'Positive signal'),
        (r'(?:unfortunately|regret|not able|no longer|position.*filled).{0,80}', 'Negative signal'),
    ]

    for pat, label in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            snippet = m.group(0).strip().replace('\n', ' ')
            snippets.append(f"{label}: …{snippet[:120]}…")

    return snippets


# ── Status inference ──────────────────────────────────────────────────────────

def _infer_status_update(text, direction, current_status):
    """Suggest a new status based on email content."""
    positive = re.search(
        r'happy to|glad to|love to|would like to|let\'s schedule|interested|look forward',
        text, re.IGNORECASE
    )
    negative = re.search(
        r'unfortunately|regret|not able|no longer|position.*filled|not moving forward|not the right fit',
        text, re.IGNORECASE
    )
    interview = re.search(r'interview|next round|speak with the team', text, re.IGNORECASE)

    if direction == 'received':
        if interview:
            return 'Active', 'Response received — interview/meeting proposed'
        if positive:
            return 'Active', 'Positive response received'
        if negative:
            return 'No Response', 'Negative/rejection signal'
        return 'Active', 'Response received'
    else:
        # Sent email
        if current_status in ('Hold', 'Cold'):
            return current_status, None
        return current_status, None  # Don't change on send


# ── Main parse function ───────────────────────────────────────────────────────

def parse_email(raw_text):
    """
    Parse raw email text. Returns a dict:
    {
      contact: Contact|None,
      confidence: 'high'|'medium'|'none',
      direction: 'sent'|'received',
      date: date,
      key_info: [str],
      suggested_status: str|None,
      status_reason: str|None,
      summary: str,          # short auto-summary for thread log
    }
    """
    text = raw_text.strip()
    contact, confidence = _match_contact(text)
    direction = _classify_direction(text)
    parsed_date = _extract_date(text)
    key_info = _extract_key_info(text)

    suggested_status = None
    status_reason = None
    if contact:
        suggested_status, status_reason = _infer_status_update(
            text, direction, contact.status
        )

    # Build a summary (first 300 chars cleaned up)
    first_content = re.sub(r'\s+', ' ', text)
    summary = first_content[:300].strip()
    if len(first_content) > 300:
        summary += "…"

    return {
        "contact": contact,
        "confidence": confidence,
        "direction": direction,
        "date": parsed_date,
        "key_info": key_info,
        "suggested_status": suggested_status,
        "status_reason": status_reason,
        "summary": summary,
        "raw_text": text,
    }
