from flask_login import UserMixin
from datetime import datetime
from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atf_id = db.Column(db.Integer, nullable=True)
    created_by = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    status = db.Column(db.String(12), nullable=False)
    position = db.Column(db.String(300), nullable=False)
    department = db.Column(db.String(300), nullable=False)
    reports_to = db.Column(db.String(300), nullable=False)
    job_location = db.Column(db.String(300), nullable=False)
    grade = db.Column(db.String(300), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False,index=True)
    job_description = db.Column(db.Text)
    job_content = db.Column(db.Text)
    job_document_name = db.Column(db.String(300), nullable=True)
    type = db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return f"Job('{self.position}','{self.department}', '{self.created_at}, '{self.due_date}')"

