"""
CareerOS — Personal Career Search Assistant
Run: python app.py
"""

import os
from datetime import date, datetime
from flask import (Flask, render_template, request, redirect,
                   url_for, flash, jsonify, Response)
from models import db, Contact, ConversationEntry, Application, CVBullet, Task
from context_export import generate_export, days_to_j1, J1_DEADLINE
from email_parser import parse_email

# ── App setup ─────────────────────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'careeros-secret-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'data', 'careeros.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# ── Template helpers ──────────────────────────────────────────────────────────

@app.context_processor
def inject_globals():
    countdown = days_to_j1()
    today_actions = Contact.query.filter(
        Contact.next_action_date == date.today(),
        Contact.status.notin_(["Cold", "Hold"])
    ).count()
    return dict(j1_countdown=countdown, today_actions=today_actions, today=date.today())


@app.template_filter('dateformat')
def dateformat(value, fmt='%b %d %Y'):
    if value is None:
        return '—'
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%Y-%m-%d').date()
        except Exception:
            return value
    return value.strftime(fmt)


@app.template_filter('days_ago')
def days_ago(value):
    if value is None:
        return '—'
    delta = (date.today() - value).days
    if delta == 0:
        return 'today'
    if delta == 1:
        return 'yesterday'
    return f'{delta}d ago'


@app.template_filter('days_until')
def days_until(value):
    if value is None:
        return '—'
    delta = (value - date.today()).days
    if delta < 0:
        return f'{abs(delta)}d overdue'
    if delta == 0:
        return 'today'
    return f'in {delta}d'


# ── Dashboard ─────────────────────────────────────────────────────────────────

@app.route('/')
def dashboard():
    today = date.today()

    # Actions due today
    due_today = Contact.query.filter(
        Contact.next_action_date == today,
        Contact.status.notin_(["Cold"])
    ).all()

    # Overdue
    overdue = Contact.query.filter(
        Contact.next_action_date < today,
        Contact.next_action_date.isnot(None),
        Contact.status.notin_(["Cold", "Hold"])
    ).order_by(Contact.next_action_date).all()

    # Due this week
    from datetime import timedelta
    week_end = today + timedelta(days=7)
    due_week = Contact.query.filter(
        Contact.next_action_date > today,
        Contact.next_action_date <= week_end,
        Contact.status.notin_(["Cold"])
    ).order_by(Contact.next_action_date).all()

    # Active contacts
    active_contacts = Contact.query.filter(
        Contact.status.in_(["Active", "Warm"])
    ).count()

    # Application stats
    total_apps = Application.query.count()
    applied_apps = Application.query.filter(
        Application.status.in_(["Applied", "Under Review", "Interview", "Offer"])
    ).count()

    # Upcoming deadlines (14 days)
    from datetime import timedelta
    deadline_window = today + timedelta(days=14)
    upcoming_deadlines = Application.query.filter(
        Application.deadline.isnot(None),
        Application.deadline <= deadline_window,
        Application.deadline >= today,
        Application.status.notin_(["Applied", "Rejected", "Withdrawn"])
    ).order_by(Application.deadline).all()

    # Tasks due today (not done)
    tasks_today = Task.query.filter(
        Task.due_date == today,
        Task.status == 'Todo'
    ).order_by(Task.priority.asc(), Task.id.asc()).all()

    # Overdue tasks
    tasks_overdue = Task.query.filter(
        Task.due_date < today,
        Task.status == 'Todo'
    ).order_by(Task.due_date.asc()).all()

    # Priority suggestions
    suggestions = _priority_suggestions(due_today, overdue, upcoming_deadlines)

    return render_template('dashboard.html',
                           due_today=due_today,
                           overdue=overdue,
                           due_week=due_week,
                           active_contacts=active_contacts,
                           total_apps=total_apps,
                           applied_apps=applied_apps,
                           upcoming_deadlines=upcoming_deadlines,
                           suggestions=suggestions,
                           tasks_today=tasks_today,
                           tasks_overdue=tasks_overdue)


def _priority_suggestions(due_today, overdue, upcoming_deadlines):
    suggestions = []
    for c in (overdue + due_today)[:3]:
        suggestions.append({
            'priority': 'high',
            'text': f"{c.name} ({c.organization or ''}): {c.next_action}",
            'contact_id': c.id,
        })
    for a in upcoming_deadlines[:2]:
        days = (a.deadline - date.today()).days
        suggestions.append({
            'priority': 'medium',
            'text': f"Apply: {a.role} @ {a.organization} — deadline in {days} days",
            'app_id': a.id,
        })
    return suggestions[:5]


# ── Contacts ──────────────────────────────────────────────────────────────────

@app.route('/contacts')
def contacts():
    status_filter = request.args.get('status', '')
    search = request.args.get('q', '').strip()
    sort = request.args.get('sort', 'action')

    q = Contact.query

    if status_filter:
        q = q.filter(Contact.status == status_filter)
    if search:
        q = q.filter(
            db.or_(
                Contact.name.ilike(f'%{search}%'),
                Contact.organization.ilike(f'%{search}%'),
                Contact.title.ilike(f'%{search}%'),
            )
        )

    contacts_list = q.all()

    STATUS_RANK = {'Active': 0, 'Pending': 1, 'Warm': 2,
                   'No Response': 3, 'Hold': 4, 'Cold': 5}

    if sort == 'action':
        def sort_key(c):
            r = STATUS_RANK.get(c.status, 6)
            d = c.next_action_date or date(2099, 12, 31)
            return (r, d)
        contacts_list.sort(key=sort_key)
    elif sort == 'name':
        contacts_list.sort(key=lambda c: c.name)
    elif sort == 'status':
        contacts_list.sort(key=lambda c: STATUS_RANK.get(c.status, 6))
    elif sort == 'recent':
        contacts_list.sort(key=lambda c: c.last_contact_date or date(2000, 1, 1), reverse=True)

    all_statuses = ['Active', 'Pending', 'Warm', 'No Response', 'Hold', 'Cold']
    return render_template('contacts.html',
                           contacts=contacts_list,
                           all_statuses=all_statuses,
                           status_filter=status_filter,
                           search=search,
                           sort=sort)


@app.route('/contacts/new', methods=['GET', 'POST'])
def new_contact():
    if request.method == 'POST':
        c = Contact(
            name=request.form['name'],
            title=request.form.get('title') or None,
            organization=request.form.get('organization') or None,
            email=request.form.get('email') or None,
            phone=request.form.get('phone') or None,
            linkedin=request.form.get('linkedin') or None,
            relationship_context=request.form.get('relationship_context') or None,
            status=request.form.get('status', 'Pending'),
            last_contact_date=_parse_form_date(request.form.get('last_contact_date')),
            next_action=request.form.get('next_action') or None,
            next_action_date=_parse_form_date(request.form.get('next_action_date')),
            notes=request.form.get('notes') or None,
        )
        db.session.add(c)
        db.session.commit()
        flash(f'Contact {c.name} added.', 'success')
        return redirect(url_for('contact_detail', contact_id=c.id))
    return render_template('contact_form.html', contact=None,
                           all_statuses=['Active', 'Pending', 'Warm', 'No Response', 'Hold', 'Cold'])


@app.route('/contacts/<int:contact_id>')
def contact_detail(contact_id):
    c = Contact.query.get_or_404(contact_id)
    entries = sorted(c.thread, key=lambda e: e.date, reverse=True)
    return render_template('contact_detail.html', contact=c, entries=entries)


@app.route('/contacts/<int:contact_id>/edit', methods=['GET', 'POST'])
def edit_contact(contact_id):
    c = Contact.query.get_or_404(contact_id)
    if request.method == 'POST':
        c.name = request.form['name']
        c.title = request.form.get('title') or None
        c.organization = request.form.get('organization') or None
        c.email = request.form.get('email') or None
        c.phone = request.form.get('phone') or None
        c.linkedin = request.form.get('linkedin') or None
        c.relationship_context = request.form.get('relationship_context') or None
        c.status = request.form.get('status', c.status)
        c.last_contact_date = _parse_form_date(request.form.get('last_contact_date'))
        c.next_action = request.form.get('next_action') or None
        c.next_action_date = _parse_form_date(request.form.get('next_action_date'))
        c.notes = request.form.get('notes') or None
        c.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Contact updated.', 'success')
        return redirect(url_for('contact_detail', contact_id=c.id))
    return render_template('contact_form.html', contact=c,
                           all_statuses=['Active', 'Pending', 'Warm', 'No Response', 'Hold', 'Cold'])


@app.route('/contacts/<int:contact_id>/log', methods=['POST'])
def add_log_entry(contact_id):
    c = Contact.query.get_or_404(contact_id)
    content = request.form.get('content', '').strip()
    if not content:
        flash('Entry cannot be empty.', 'warning')
        return redirect(url_for('contact_detail', contact_id=contact_id))

    entry = ConversationEntry(
        contact_id=c.id,
        date=_parse_form_date(request.form.get('entry_date')) or date.today(),
        entry_type=request.form.get('entry_type', 'note'),
        content=content,
    )
    db.session.add(entry)

    # Update contact fields
    new_status = request.form.get('new_status')
    if new_status and new_status != c.status:
        c.status = new_status
    c.last_contact_date = entry.date
    next_action = request.form.get('next_action', '').strip()
    c.next_action = next_action or None
    c.next_action_date = _parse_form_date(request.form.get('next_action_date'))
    c.updated_at = datetime.utcnow()

    db.session.commit()
    flash('Entry logged.', 'success')
    return redirect(url_for('contact_detail', contact_id=contact_id))


@app.route('/contacts/<int:contact_id>/delete', methods=['POST'])
def delete_contact(contact_id):
    c = Contact.query.get_or_404(contact_id)
    name = c.name
    db.session.delete(c)
    db.session.commit()
    flash(f'Contact {name} deleted.', 'info')
    return redirect(url_for('contacts'))


# ── Applications ──────────────────────────────────────────────────────────────

@app.route('/applications')
def applications():
    status_filter = request.args.get('status', '')
    lane_filter = request.args.get('lane', '')
    search = request.args.get('q', '').strip()

    q = Application.query

    if status_filter:
        q = q.filter(Application.status == status_filter)
    if lane_filter:
        q = q.filter(Application.lane == lane_filter)
    if search:
        q = q.filter(
            db.or_(
                Application.role.ilike(f'%{search}%'),
                Application.organization.ilike(f'%{search}%'),
            )
        )

    apps = q.all()
    STATUS_ORDER = {'Applied': 0, 'Under Review': 1, 'Interview': 2, 'Offer': 3,
                    'Drafting': 4, 'Decided-After-Call': 5, 'Rejected': 6, 'Withdrawn': 7}
    apps.sort(key=lambda a: (STATUS_ORDER.get(a.status, 9), a.applied_date or date(2099, 1, 1)))

    all_statuses = ['Drafting', 'Applied', 'Under Review', 'Interview', 'Offer',
                    'Decided-After-Call', 'Rejected', 'Withdrawn']
    all_lanes = sorted(set(a.lane for a in Application.query.all() if a.lane))

    return render_template('applications.html',
                           apps=apps,
                           all_statuses=all_statuses,
                           all_lanes=all_lanes,
                           status_filter=status_filter,
                           lane_filter=lane_filter,
                           search=search)


@app.route('/applications/new', methods=['GET', 'POST'])
def new_application():
    if request.method == 'POST':
        a = Application(
            role=request.form['role'],
            organization=request.form.get('organization') or None,
            req_number=request.form.get('req_number') or None,
            status=request.form.get('status', 'Drafting'),
            deadline=_parse_form_date(request.form.get('deadline')),
            applied_date=_parse_form_date(request.form.get('applied_date')),
            location=request.form.get('location') or None,
            salary_range=request.form.get('salary_range') or None,
            notes=request.form.get('notes') or None,
            resume_version=request.form.get('resume_version') or None,
            lane=request.form.get('lane') or None,
            job_description=request.form.get('job_description') or None,
        )
        db.session.add(a)
        db.session.commit()
        flash(f'Application added: {a.role}', 'success')
        return redirect(url_for('applications'))
    all_statuses = ['Drafting', 'Applied', 'Under Review', 'Interview', 'Offer',
                    'Decided-After-Call', 'Rejected', 'Withdrawn']
    return render_template('app_form.html', app=None, all_statuses=all_statuses)


@app.route('/applications/<int:app_id>/edit', methods=['GET', 'POST'])
def edit_application(app_id):
    a = Application.query.get_or_404(app_id)
    all_statuses = ['Drafting', 'Applied', 'Under Review', 'Interview', 'Offer',
                    'Decided-After-Call', 'Rejected', 'Withdrawn']
    if request.method == 'POST':
        a.role = request.form['role']
        a.organization = request.form.get('organization') or None
        a.req_number = request.form.get('req_number') or None
        a.status = request.form.get('status', a.status)
        a.deadline = _parse_form_date(request.form.get('deadline'))
        a.applied_date = _parse_form_date(request.form.get('applied_date'))
        a.location = request.form.get('location') or None
        a.salary_range = request.form.get('salary_range') or None
        a.notes = request.form.get('notes') or None
        a.resume_version = request.form.get('resume_version') or None
        a.lane = request.form.get('lane') or None
        a.job_description = request.form.get('job_description') or None
        a.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Application updated.', 'success')
        return redirect(url_for('applications'))
    return render_template('app_form.html', app=a, all_statuses=all_statuses)


@app.route('/applications/<int:app_id>/delete', methods=['POST'])
def delete_application(app_id):
    a = Application.query.get_or_404(app_id)
    db.session.delete(a)
    db.session.commit()
    flash('Application deleted.', 'info')
    return redirect(url_for('applications'))


@app.route('/applications/dedup', methods=['POST'])
def dedup_applications():
    """Remove duplicate applications, keeping the one with the lowest id."""
    from sqlalchemy import func
    seen = {}
    removed = 0
    for a in Application.query.order_by(Application.id).all():
        key = (a.role.strip().lower(), (a.organization or '').strip().lower())
        if key in seen:
            db.session.delete(a)
            removed += 1
        else:
            seen[key] = a.id
    db.session.commit()
    flash(f'Removed {removed} duplicate application(s).', 'success' if removed else 'info')
    return redirect(url_for('applications'))


# ── Email Ingestion ───────────────────────────────────────────────────────────

@app.route('/email', methods=['GET', 'POST'])
def email_ingest():
    result = None
    if request.method == 'POST':
        raw = request.form.get('email_text', '').strip()
        if raw:
            result = parse_email(raw)
            if request.form.get('confirm_save') == '1':
                # Save to DB
                contact = result['contact']
                if request.form.get('contact_id'):
                    contact = Contact.query.get(int(request.form['contact_id']))
                if contact is None and request.form.get('new_contact_name'):
                    contact = Contact(
                        name=request.form['new_contact_name'],
                        organization=request.form.get('new_contact_org') or None,
                        status='Pending',
                    )
                    db.session.add(contact)
                    db.session.flush()

                if contact:
                    entry = ConversationEntry(
                        contact_id=contact.id,
                        date=result['date'],
                        entry_type=result['direction'],
                        content=request.form.get('final_content') or result['summary'],
                    )
                    db.session.add(entry)

                    # Update contact status/dates
                    if result['suggested_status'] and result['suggested_status'] != contact.status:
                        if request.form.get('apply_status') == '1':
                            contact.status = result['suggested_status']
                    contact.last_contact_date = result['date']
                    if request.form.get('next_action'):
                        contact.next_action = request.form['next_action']
                    if request.form.get('next_action_date'):
                        contact.next_action_date = _parse_form_date(request.form['next_action_date'])
                    contact.updated_at = datetime.utcnow()

                    db.session.commit()
                    flash(f'Email logged to {contact.name}.', 'success')
                    return redirect(url_for('contact_detail', contact_id=contact.id))

        all_contacts = Contact.query.order_by(Contact.name).all()
        return render_template('email_ingest.html', result=result,
                               raw=raw, all_contacts=all_contacts)

    all_contacts = Contact.query.order_by(Contact.name).all()
    return render_template('email_ingest.html', result=None,
                           raw='', all_contacts=all_contacts)


# ── CSV Upload ────────────────────────────────────────────────────────────────

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    results = []
    if request.method == 'POST':
        from csv_importer import run_all_imports
        import tempfile, csv as csv_module

        uploaded_file = request.files.get('csv_file')
        upload_type = request.form.get('upload_type', 'contacts')

        if uploaded_file and uploaded_file.filename:
            # Save to temp file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False,
                                             encoding='utf-8') as tmp:
                content = uploaded_file.read().decode('utf-8-sig')
                tmp.write(content)
                tmp_path = tmp.name

            from csv_importer import import_applications, import_outreach, import_weekly_tracker
            if upload_type == 'applications':
                count, err = import_applications(tmp_path)
            elif upload_type == 'weekly':
                count, err = import_weekly_tracker(tmp_path)
            else:
                count, err = import_outreach(tmp_path)

            os.unlink(tmp_path)

            if err:
                flash(f'Import error: {err}', 'danger')
            else:
                flash(f'Imported {count} new records.', 'success')

        elif request.form.get('run_auto_import'):
            # Auto-import from same directory
            results = run_all_imports(BASE_DIR)
            for fname, count, err in results:
                if err:
                    flash(f'{fname}: {err}', 'warning')
                else:
                    flash(f'{fname}: {count} new records imported.', 'success')

    return render_template('upload.html', results=results)


# ── Context Export ────────────────────────────────────────────────────────────

@app.route('/export')
def export():
    md = generate_export()
    return render_template('export.html', markdown_content=md, countdown=days_to_j1())


@app.route('/export/download')
def export_download():
    md = generate_export()
    filename = f"careeros_context_{date.today().isoformat()}.md"
    return Response(
        md,
        mimetype='text/markdown',
        headers={'Content-Disposition': f'attachment; filename="{filename}"'}
    )


# ── Resume Builder (stub — full build is Phase 3) ─────────────────────────────

@app.route('/resume')
def resume():
    bullets = CVBullet.query.order_by(CVBullet.employer, CVBullet.id).all()
    employers = list(dict.fromkeys(b.employer for b in bullets))
    return render_template('resume.html', bullets=bullets, employers=employers, tailored=None, jd='')


@app.route('/resume/tailor', methods=['POST'])
def tailor_resume():
    jd = request.form.get('jd', '').strip()
    bullets = CVBullet.query.all()
    tailored = _score_bullets(jd, bullets) if jd else []
    employers = list(dict.fromkeys(b.employer for b in CVBullet.query.order_by(CVBullet.employer).all()))
    return render_template('resume.html', bullets=CVBullet.query.all(),
                           employers=employers, tailored=tailored, jd=jd)


@app.route('/resume/bullet/new', methods=['POST'])
def add_bullet():
    b = CVBullet(
        employer=request.form['employer'],
        period=request.form.get('period') or None,
        bullet_text=request.form['bullet_text'],
        tags=request.form.get('tags') or None,
    )
    db.session.add(b)
    db.session.commit()
    flash('Bullet added.', 'success')
    return redirect(url_for('resume'))


@app.route('/resume/bullet/<int:bullet_id>/delete', methods=['POST'])
def delete_bullet(bullet_id):
    b = CVBullet.query.get_or_404(bullet_id)
    db.session.delete(b)
    db.session.commit()
    flash('Bullet deleted.', 'info')
    return redirect(url_for('resume'))


def _score_bullets(jd, bullets):
    """Keyword-based scoring of CV bullets against a job description."""
    import re
    jd_words = set(re.findall(r'\b\w{4,}\b', jd.lower()))
    stop = {'with', 'that', 'this', 'from', 'have', 'will', 'your', 'their',
            'they', 'them', 'been', 'were', 'into', 'about', 'more', 'also',
            'such', 'each', 'over', 'than', 'when', 'well', 'role', 'team',
            'work', 'experience', 'skills', 'strong', 'ability', 'including'}
    jd_words -= stop

    scored = []
    for b in bullets:
        bullet_words = set(re.findall(r'\b\w{4,}\b', b.bullet_text.lower()))
        tag_words = set(re.findall(r'\b\w{4,}\b', (b.tags or '').lower()))
        all_words = bullet_words | tag_words
        hits = jd_words & all_words
        score = len(hits)
        if score > 0:
            scored.append({'bullet': b, 'score': score, 'hits': sorted(hits)})

    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:20]


# ── Tasks ─────────────────────────────────────────────────────────────────────

ALL_CATEGORIES = ['Career', 'Personal', 'Academic']
ALL_PRIORITIES = ['High', 'Medium', 'Low']
ALL_TASK_STATUSES = ['Todo', 'Done', 'Skipped']


@app.route('/tasks')
def tasks():
    status_filter = request.args.get('status', 'Todo')
    category_filter = request.args.get('category', '')

    q = Task.query
    if status_filter:
        q = q.filter(Task.status == status_filter)
    if category_filter:
        q = q.filter(Task.category == category_filter)

    all_tasks = q.order_by(Task.due_date.asc().nullslast(), Task.priority.asc(), Task.id.asc()).all()

    return render_template('tasks.html',
                           tasks=all_tasks,
                           status_filter=status_filter,
                           category_filter=category_filter,
                           all_categories=ALL_CATEGORIES,
                           all_priorities=ALL_PRIORITIES,
                           all_statuses=ALL_TASK_STATUSES,
                           all_contacts=Contact.query.order_by(Contact.name).all(),
                           all_apps=Application.query.order_by(Application.role).all())


@app.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        t = Task(
            title=request.form['title'],
            due_date=_parse_form_date(request.form.get('due_date')),
            time_estimate=request.form.get('time_estimate') or None,
            category=request.form.get('category', 'Career'),
            priority=request.form.get('priority', 'Medium'),
            status='Todo',
            linked_contact_id=int(request.form['linked_contact_id']) if request.form.get('linked_contact_id') else None,
            linked_application_id=int(request.form['linked_application_id']) if request.form.get('linked_application_id') else None,
            notes=request.form.get('notes') or None,
        )
        db.session.add(t)
        db.session.commit()
        flash('Task added.', 'success')
        return redirect(request.form.get('next') or url_for('tasks'))
    return render_template('task_form.html', task=None,
                           all_categories=ALL_CATEGORIES, all_priorities=ALL_PRIORITIES,
                           all_contacts=Contact.query.order_by(Contact.name).all(),
                           all_apps=Application.query.order_by(Application.role).all())


@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    t = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        t.title = request.form['title']
        t.due_date = _parse_form_date(request.form.get('due_date'))
        t.time_estimate = request.form.get('time_estimate') or None
        t.category = request.form.get('category', t.category)
        t.priority = request.form.get('priority', t.priority)
        t.status = request.form.get('status', t.status)
        t.linked_contact_id = int(request.form['linked_contact_id']) if request.form.get('linked_contact_id') else None
        t.linked_application_id = int(request.form['linked_application_id']) if request.form.get('linked_application_id') else None
        t.notes = request.form.get('notes') or None
        t.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Task updated.', 'success')
        return redirect(url_for('tasks'))
    return render_template('task_form.html', task=t,
                           all_categories=ALL_CATEGORIES, all_priorities=ALL_PRIORITIES,
                           all_statuses=ALL_TASK_STATUSES,
                           all_contacts=Contact.query.order_by(Contact.name).all(),
                           all_apps=Application.query.order_by(Application.role).all())


@app.route('/tasks/<int:task_id>/done', methods=['POST'])
def toggle_task_done(task_id):
    t = Task.query.get_or_404(task_id)
    t.status = 'Todo' if t.status == 'Done' else 'Done'
    t.updated_at = datetime.utcnow()
    db.session.commit()
    return redirect(request.referrer or url_for('tasks'))


@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    t = Task.query.get_or_404(task_id)
    db.session.delete(t)
    db.session.commit()
    flash('Task deleted.', 'info')
    return redirect(request.referrer or url_for('tasks'))


# ── DB Init + Seed ────────────────────────────────────────────────────────────

def init_db():
    db.create_all()
    _seed_if_empty()
    # Auto-import CSVs from app directory
    from csv_importer import run_all_imports
    results = run_all_imports(BASE_DIR)
    for fname, count, err in results:
        if not err and count:
            print(f"  [CSV] {fname}: {count} records imported")


def _seed_if_empty():
    from seed_data import SEED_CONTACTS, SEED_APPLICATIONS, CV_BULLETS, SEED_TASKS

    if Contact.query.count() == 0:
        print("  [seed] Populating initial contacts and CV bullets…")

        for cd in SEED_CONTACTS:
            c = Contact(
                name=cd['name'],
                title=cd.get('title'),
                organization=cd.get('organization'),
                email=cd.get('email') or None,
                relationship_context=cd.get('relationship_context'),
                status=cd.get('status', 'Pending'),
                last_contact_date=cd.get('last_contact_date'),
                next_action=cd.get('next_action'),
                next_action_date=cd.get('next_action_date'),
            )
            db.session.add(c)
            db.session.flush()
            for te in cd.get('thread', []):
                entry = ConversationEntry(
                    contact_id=c.id,
                    date=te['date'],
                    entry_type=te['entry_type'],
                    content=te['content'],
                )
                db.session.add(entry)

        for bd in CV_BULLETS:
            b = CVBullet(
                employer=bd['employer'],
                period=bd.get('period'),
                bullet_text=bd['bullet_text'],
                tags=bd.get('tags'),
            )
            db.session.add(b)

        db.session.commit()
        print(f"  [seed] Done: {len(SEED_CONTACTS)} contacts, {len(CV_BULLETS)} CV bullets")

    if Application.query.count() == 0:
        for ad in SEED_APPLICATIONS:
            a = Application(
                role=ad['role'],
                organization=ad.get('organization'),
                req_number=ad.get('req_number') or None,
                status=ad.get('status', 'Drafting'),
                applied_date=ad.get('applied_date'),
                deadline=ad.get('deadline'),
                location=ad.get('location'),
                notes=ad.get('notes'),
                lane=ad.get('lane'),
            )
            db.session.add(a)
        db.session.commit()
        print(f"  [seed] {len(SEED_APPLICATIONS)} applications seeded")

    if Task.query.count() == 0:
        # Build a name→id lookup for contacts already in DB
        contact_lookup = {c.name: c.id for c in Contact.query.all()}
        for td in SEED_TASKS:
            linked_id = None
            if td.get('linked_contact'):
                linked_id = contact_lookup.get(td['linked_contact'])
            t = Task(
                title=td['title'],
                due_date=td.get('due_date'),
                time_estimate=td.get('time_estimate'),
                category=td.get('category', 'Career'),
                priority=td.get('priority', 'Medium'),
                status=td.get('status', 'Todo'),
                notes=td.get('notes'),
                linked_contact_id=linked_id,
            )
            db.session.add(t)
        db.session.commit()
        print(f"  [seed] {len(SEED_TASKS)} tasks seeded")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _parse_form_date(val):
    if not val or val.strip() == '':
        return None
    try:
        return datetime.strptime(val.strip(), '%Y-%m-%d').date()
    except ValueError:
        return None


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)
    with app.app_context():
        init_db()
    print("\n  CareerOS running at http://localhost:5000\n")
    app.run(debug=True, port=5000)
