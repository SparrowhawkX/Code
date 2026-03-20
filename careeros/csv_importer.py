"""
CSV importer for CareerOS.
Handles three CSVs: applications_clean.csv, outreach_clean.csv, weekly_tracker_clean.csv
All imports are idempotent — existing rows matched by name/role+org are updated, not duplicated.
"""

import csv
import os
from datetime import date, datetime
from models import db, Contact, ConversationEntry, Application


def _parse_date(val):
    if not val or str(val).strip() in ("", "nan", "None", "N/A", "-"):
        return None
    val = str(val).strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%d-%b-%Y", "%b %d %Y", "%d %b %Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(val, fmt).date()
        except ValueError:
            continue
    # Try truncating time component
    try:
        return datetime.strptime(val[:10], "%Y-%m-%d").date()
    except Exception:
        return None


def _get(row, *keys, default=""):
    """Case-insensitive key lookup on a dict row."""
    row_lower = {k.lower().strip(): v for k, v in row.items()}
    for k in keys:
        v = row_lower.get(k.lower().strip())
        if v is not None:
            return str(v).strip()
    return default


def _find_or_create_contact(name, org="", title=""):
    """Match existing contact by normalised name; create shell if not found."""
    if not name:
        return None
    norm = name.lower().strip()
    existing = Contact.query.all()
    for c in existing:
        if c.name.lower().strip() == norm:
            return c
    # Create new
    c = Contact(name=name, organization=org or None, title=title or None)
    db.session.add(c)
    db.session.flush()
    return c


def import_applications(filepath):
    """Import applications_clean.csv"""
    if not os.path.exists(filepath):
        return 0, f"File not found: {filepath}"

    imported = 0
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            role = _get(row, "role", "position", "title", "job title")
            org  = _get(row, "organization", "org", "company", "employer")
            req  = _get(row, "req_number", "req number", "req", "requisition", "job id", "jobid")
            status     = _get(row, "status", default="Applied")
            deadline   = _parse_date(_get(row, "deadline", "due date", "close date"))
            applied    = _parse_date(_get(row, "applied_date", "date applied", "applied", "date"))
            notes      = _get(row, "notes", "comments", "note")
            lane       = _get(row, "lane", "track", "tier")
            location   = _get(row, "location", "city", "country")
            resume_ver = _get(row, "resume_version", "resume", "cv version")

            if not role:
                continue

            # Dedup: match on (role, org) case-insensitive
            existing = Application.query.filter(
                db.func.lower(Application.role) == role.lower(),
                db.func.lower(Application.organization) == org.lower()
            ).first()

            if existing:
                # Update fields that are empty
                if not existing.req_number and req:
                    existing.req_number = req
                if not existing.deadline and deadline:
                    existing.deadline = deadline
                if not existing.applied_date and applied:
                    existing.applied_date = applied
                if not existing.lane and lane:
                    existing.lane = lane
                if not existing.location and location:
                    existing.location = location
                if notes and existing.notes and notes not in existing.notes:
                    existing.notes = (existing.notes or "") + "\n[CSV] " + notes
                elif not existing.notes and notes:
                    existing.notes = notes
            else:
                app = Application(
                    role=role,
                    organization=org or None,
                    req_number=req or None,
                    status=status or "Applied",
                    deadline=deadline,
                    applied_date=applied,
                    notes=notes or None,
                    lane=lane or None,
                    location=location or None,
                    resume_version=resume_ver or None,
                )
                db.session.add(app)
                imported += 1

    db.session.commit()
    return imported, None


def import_outreach(filepath):
    """Import outreach_clean.csv — adds contacts with initial thread entries."""
    if not os.path.exists(filepath):
        return 0, f"File not found: {filepath}"

    imported = 0
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name   = _get(row, "name", "contact name", "contact")
            title  = _get(row, "title", "position", "role")
            org    = _get(row, "organization", "org", "company")
            email  = _get(row, "email")
            status = _get(row, "status", default="Pending")
            ctx    = _get(row, "context", "relationship_context", "relationship", "notes", "note")
            last   = _parse_date(_get(row, "last_contact", "last_contact_date", "last contact", "date"))
            next_a = _get(row, "next_action", "action", "next step")
            next_d = _parse_date(_get(row, "next_action_date", "next date", "follow up date"))
            content = _get(row, "thread", "message", "content", "last message")
            entry_type = _get(row, "type", "entry_type", default="note")

            if not name:
                continue

            c = _find_or_create_contact(name, org, title)
            created_new = not c.relationship_context

            if title and not c.title:
                c.title = title
            if org and not c.organization:
                c.organization = org
            if email and not c.email:
                c.email = email
            if ctx and not c.relationship_context:
                c.relationship_context = ctx
            if status and (not c.status or c.status == "Pending"):
                c.status = status
            if last and not c.last_contact_date:
                c.last_contact_date = last
            if next_a and not c.next_action:
                c.next_action = next_a
            if next_d and not c.next_action_date:
                c.next_action_date = next_d

            # Add thread entry if content provided
            if content:
                entry_date = last or date.today()
                existing_entry = ConversationEntry.query.filter_by(
                    contact_id=c.id, content=content
                ).first()
                if not existing_entry:
                    entry = ConversationEntry(
                        contact_id=c.id,
                        date=entry_date,
                        entry_type=entry_type or "note",
                        content=content,
                    )
                    db.session.add(entry)

            if created_new:
                imported += 1

    db.session.commit()
    return imported, None


def import_weekly_tracker(filepath):
    """
    Import weekly_tracker_clean.csv — 30 weeks of activity.
    Best-effort: if a contact name matches, append thread entries.
    """
    if not os.path.exists(filepath):
        return 0, f"File not found: {filepath}"

    imported = 0
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name    = _get(row, "name", "contact", "contact name")
            content = _get(row, "activity", "action", "note", "content", "message", "summary")
            entry_type = _get(row, "type", "entry_type", "channel", default="note")
            d       = _parse_date(_get(row, "date", "week", "week_start", "week_ending"))
            status  = _get(row, "status")

            if not name or not content:
                continue

            c = _find_or_create_contact(name)
            if not c:
                continue

            # Update status if provided and more specific
            if status and status not in ("", "nan"):
                c.status = status

            # Avoid exact duplicate entries
            existing = ConversationEntry.query.filter_by(
                contact_id=c.id, content=content
            ).first()
            if not existing:
                entry = ConversationEntry(
                    contact_id=c.id,
                    date=d or date.today(),
                    entry_type=entry_type or "note",
                    content=content,
                )
                db.session.add(entry)
                imported += 1

    db.session.commit()
    return imported, None


def run_all_imports(base_dir="."):
    """Run all three CSV imports. Returns list of (filename, count, error) tuples."""
    results = []
    for fname, fn in [
        ("applications_clean.csv", import_applications),
        ("outreach_clean.csv",     import_outreach),
        ("weekly_tracker_clean.csv", import_weekly_tracker),
    ]:
        path = os.path.join(base_dir, fname)
        count, err = fn(path)
        results.append((fname, count, err))
    return results
