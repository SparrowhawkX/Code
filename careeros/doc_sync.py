"""
Document sync — extract text from .docx and parse with Claude API.
No DB access here; all DB logic lives in app.py.
"""

import zipfile
import xml.etree.ElementTree as ET
import json
import re


def extract_docx_text(file_path):
    """Extract plain text from a .docx file without requiring python-docx."""
    with zipfile.ZipFile(file_path) as z:
        with z.open('word/document.xml') as f:
            tree = ET.parse(f)
    ns = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    root = tree.getroot()
    lines = []
    for para in root.iter(f'{{{ns}}}p'):
        runs = para.findall(f'.//{{{ns}}}t')
        line = ''.join(r.text or '' for r in runs)
        lines.append(line)
    return '\n'.join(lines)


def parse_context_document(text, api_key):
    """
    Send document text to Claude Haiku and return structured data.
    Returns dict with keys: contacts, applications, tasks.
    Each is a list of dicts matching the CareerOS schema.
    """
    from anthropic import Anthropic

    client = Anthropic(api_key=api_key)

    system = (
        "You are a data extraction assistant for a personal job search tracker called CareerOS. "
        "Extract structured data from career search context documents. "
        "Return only valid JSON — no markdown fences, no explanation, no extra text."
    )

    prompt = f"""Extract all contacts, job applications, and tasks from this career search document.

Return a single JSON object with exactly three keys: "contacts", "applications", "tasks".

"contacts" — array of objects:
  name (string, required)
  title (string or null)
  organization (string or null)
  status: one of Active | Pending | Warm | No Response | Hold | Cold
  last_contact_date: "YYYY-MM-DD" or null
  next_action: string or null
  next_action_date: "YYYY-MM-DD" or null
  relationship_context: string or null
  latest_thread_entry: object with keys date ("YYYY-MM-DD"), type (call|sent|received|note|linkedin|whatsapp), content (string) — or null

"applications" — array of objects:
  role (string, required)
  organization: string or null
  req_number: string or null
  status: one of Drafting | Applied | Under Review | Interview | Offer | Rejected | Withdrawn
  applied_date: "YYYY-MM-DD" or null
  deadline: "YYYY-MM-DD" or null
  location: string or null
  notes: string or null
  resume_version: string or null
  lane: one of Multilateral | India Private | US Private | Think Tank | null

"tasks" — array of objects:
  title (string, required)
  category: one of Career | Personal | Academic
  priority: one of High | Medium | Low
  due_date: "YYYY-MM-DD" or null
  time_estimate: string or null  (e.g. "15 min", "1 hr")
  notes: string or null
  linked_contact_name: string matching a contact name above, or null

Document text:
{text}"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=8192,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    # Strip markdown code fences if model adds them despite instructions
    raw = re.sub(r'^```(?:json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)

    return json.loads(raw)
