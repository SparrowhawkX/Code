from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(300))
    organization = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(100))
    linkedin = db.Column(db.String(400))
    relationship_context = db.Column(db.Text)
    status = db.Column(db.String(50), default='Pending')
    # Active / Pending / Warm / No Response / Hold / Cold
    last_contact_date = db.Column(db.Date)
    next_action = db.Column(db.Text)
    next_action_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    thread = db.relationship(
        'ConversationEntry',
        backref='contact',
        lazy=True,
        cascade='all, delete-orphan',
        order_by='ConversationEntry.date.desc()'
    )

    def status_badge(self):
        return {
            'Active':      'success',
            'Pending':     'warning',
            'Warm':        'info',
            'No Response': 'danger',
            'Hold':        'secondary',
            'Cold':        'dark',
        }.get(self.status, 'light')

    def days_since_contact(self):
        if self.last_contact_date:
            return (date.today() - self.last_contact_date).days
        return None

    def __repr__(self):
        return f'<Contact {self.name}>'


class ConversationEntry(db.Model):
    __tablename__ = 'conversation_entries'

    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    entry_type = db.Column(db.String(50), default='note')
    # sent / received / call / note / linkedin / whatsapp
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Entry {self.entry_type} {self.date}>'


class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(400), nullable=False)
    organization = db.Column(db.String(200))
    req_number = db.Column(db.String(100))
    status = db.Column(db.String(100), default='Drafting')
    # Drafting / Applied / Under Review / Interview / Offer / Rejected / Withdrawn / Decided-After-Call
    deadline = db.Column(db.Date)
    applied_date = db.Column(db.Date)
    location = db.Column(db.String(200))
    salary_range = db.Column(db.String(100))
    notes = db.Column(db.Text)
    resume_version = db.Column(db.String(100))
    lane = db.Column(db.String(100))
    # Lane A / Lane B / Lane C etc. from CSV
    job_description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def status_badge(self):
        return {
            'Applied':            'primary',
            'Drafting':           'warning',
            'Under Review':       'info',
            'Interview':          'success',
            'Offer':              'success',
            'Rejected':           'danger',
            'Withdrawn':          'secondary',
            'Decided-After-Call': 'warning',
        }.get(self.status, 'light')

    def __repr__(self):
        return f'<Application {self.role} @ {self.organization}>'


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date)
    time_estimate = db.Column(db.String(50))   # e.g. "10 min", "3–4 hours"
    category = db.Column(db.String(50), default='Career')
    # Career / Personal / Academic
    status = db.Column(db.String(20), default='Todo')
    # Todo / Done / Skipped
    priority = db.Column(db.String(20), default='Medium')
    # High / Medium / Low
    linked_contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=True)
    linked_application_id = db.Column(db.Integer, db.ForeignKey('applications.id'), nullable=True)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    linked_contact = db.relationship('Contact', foreign_keys=[linked_contact_id])
    linked_application = db.relationship('Application', foreign_keys=[linked_application_id])

    def category_icon(self):
        return {'Career': '💼', 'Personal': '🏠', 'Academic': '📚'}.get(self.category, '📌')

    def priority_badge(self):
        return {'High': 'danger', 'Medium': 'warning', 'Low': 'secondary'}.get(self.priority, 'light')

    def __repr__(self):
        return f'<Task {self.title[:40]}>'


class CVBullet(db.Model):
    __tablename__ = 'cv_bullets'

    id = db.Column(db.Integer, primary_key=True)
    employer = db.Column(db.String(200), nullable=False)
    period = db.Column(db.String(100))
    bullet_text = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(1000))
    # comma-separated keywords for matching
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def tag_list(self):
        if self.tags:
            return [t.strip() for t in self.tags.split(',')]
        return []

    def __repr__(self):
        return f'<CVBullet {self.employer}: {self.bullet_text[:60]}>'
