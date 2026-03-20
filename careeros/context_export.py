"""
Context export — generates a single markdown file you can paste into any new
Claude conversation to instantly orient the AI without re-explaining anything.
"""

from datetime import date
from models import Contact, Application, ConversationEntry

J1_DEADLINE = date(2026, 6, 27)

PROFILE = """# CareerOS Context Export

## Who I Am
- **Name:** Indian national, 39, graduating Harvard Kennedy School MPA/ID May 2026
- **Visa:** J-1 — must have job offer by **June 27 2026**
- **Family:** Wife and 3-year-old daughter
- **Locations open to:** DC, NY, Europe, Singapore, Middle East, India
- **Salary floor:** $150,000 USD
- **Graduating:** May 2026, HKS MPA/ID

## Background (15+ years energy policy)
- **Private sector:** Welspun Energy (2011–2016), Reliance Infrastructure (2009–2011)
- **Government of India MNRE (2016–2024):** Led $2.1B National Green Hydrogen Mission, $9B solar rooftop program, transmission pricing reform, $3B World Bank PforR
- **WRI India (2024):** Hydrogen & energy storage
- **World Bank ESMAP consultant (2025):** Hydrogen in emerging markets
- **Harvard Belfer Center (2025–present):** AI/data centers/US grid research
- **Publications:** Two Belfer policy briefs (AI + US grid), SYPA "Cables Before Compute", SSRN working paper on green hydrogen

## Priority Lanes
- **Lane A (Top):** World Bank KIEPR, E3 Associate Director, Avina, Google, IRENA, WRI
- **Lane B:** ADB Fast-Track, WB ECA Vienna/Serbia, IFC climate/energy roles
- **Lane C:** IMF, others

"""


def days_to_j1():
    return (J1_DEADLINE - date.today()).days


def _status_rank(status):
    return {"Active": 0, "Pending": 1, "Warm": 2, "No Response": 3, "Hold": 4, "Cold": 5}.get(status, 6)


def generate_export():
    today = date.today()
    countdown = days_to_j1()

    lines = [PROFILE]
    lines.append(f"## J-1 Countdown\n**{countdown} days** remaining until June 27 2026 deadline.\n")

    # ── Contacts ──────────────────────────────────────────────────────────────
    lines.append("\n## Active Contacts (sorted by priority)\n")
    contacts = Contact.query.all()
    contacts.sort(key=lambda c: (_status_rank(c.status), c.name))

    for c in contacts:
        if c.status == "Cold":
            continue  # skip cold contacts from export
        lines.append(f"### {c.name}")
        parts = [p for p in [c.title, c.organization] if p]
        if parts:
            lines.append(f"**{' | '.join(parts)}**")
        if c.email:
            lines.append(f"Email: {c.email}")
        lines.append(f"Status: **{c.status}**")
        if c.last_contact_date:
            delta = (today - c.last_contact_date).days
            lines.append(f"Last contact: {c.last_contact_date.strftime('%b %d %Y')} ({delta} days ago)")
        if c.next_action:
            nd = c.next_action_date.strftime('%b %d') if c.next_action_date else "TBD"
            lines.append(f"Next action ({nd}): {c.next_action}")
        if c.relationship_context:
            lines.append(f"Context: {c.relationship_context}")
        # Last 3 thread entries
        entries = sorted(c.thread, key=lambda e: e.date, reverse=True)[:3]
        if entries:
            lines.append("Recent thread:")
            for e in entries:
                lines.append(f"  - [{e.date.strftime('%Y-%m-%d')} {e.entry_type}] {e.content}")
        lines.append("")

    # ── Applications ─────────────────────────────────────────────────────────
    lines.append("\n## Applications\n")
    apps = Application.query.order_by(Application.applied_date.desc().nullslast()).all()

    status_order = {"Applied": 0, "Under Review": 1, "Interview": 2, "Offer": 3,
                    "Drafting": 4, "Decided-After-Call": 5, "Rejected": 6, "Withdrawn": 7}
    apps.sort(key=lambda a: status_order.get(a.status, 9))

    for a in apps:
        lane = f" [{a.lane}]" if a.lane else ""
        req  = f" ({a.req_number})" if a.req_number else ""
        lines.append(f"- **{a.role}** @ {a.organization or 'TBD'}{req}{lane} — {a.status}")
        if a.applied_date:
            lines.append(f"  Applied: {a.applied_date.strftime('%b %d %Y')}")
        if a.deadline:
            dl_days = (a.deadline - today).days
            lines.append(f"  Deadline: {a.deadline.strftime('%b %d %Y')} ({dl_days} days)")
        if a.location:
            lines.append(f"  Location: {a.location}")
        if a.notes:
            lines.append(f"  Notes: {a.notes}")
        lines.append("")

    # ── Priority Actions This Week ────────────────────────────────────────────
    lines.append("\n## Priority Actions This Week\n")
    week_contacts = [
        c for c in contacts
        if c.next_action_date and c.next_action_date >= today
           and (c.next_action_date - today).days <= 7
           and c.status not in ("Cold", "Hold")
    ]
    week_contacts.sort(key=lambda c: c.next_action_date)

    for c in week_contacts:
        nd = c.next_action_date.strftime('%a %b %d')
        lines.append(f"- **{nd}** | {c.name} ({c.organization or ''}): {c.next_action}")

    # Overdue actions
    overdue = [
        c for c in contacts
        if c.next_action_date and c.next_action_date < today
           and c.status not in ("Cold", "Hold")
    ]
    if overdue:
        lines.append("\n**Overdue actions:**")
        for c in overdue:
            lines.append(f"- ⚠️ {c.name}: {c.next_action} (was due {c.next_action_date.strftime('%b %d')})")

    # Deadlines
    upcoming_deadlines = [
        a for a in apps
        if a.deadline and (a.deadline - today).days <= 14 and a.status not in ("Applied", "Rejected", "Withdrawn")
    ]
    if upcoming_deadlines:
        lines.append("\n**Upcoming application deadlines:**")
        for a in sorted(upcoming_deadlines, key=lambda x: x.deadline):
            dl_days = (a.deadline - today).days
            lines.append(f"- {a.role} @ {a.organization}: {a.deadline.strftime('%b %d')} ({dl_days} days)")

    lines.append(f"\n---\n*Generated {today.strftime('%B %d, %Y')} | J-1 deadline: June 27 2026 ({countdown} days)*\n")

    return "\n".join(lines)
