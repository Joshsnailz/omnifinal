from flask_login import UserMixin
from datetime import datetime
from app import db


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_fullname = db.Column(db.String(500), nullable=False, unique=True)
    role_shortcut = db.Column(db.String(500), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(500),unique=True, nullable=False)
    profile_pic = db.Column(db.String(50),nullable=True, default='default.png')
    password = db.Column(db.String(160),nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship("Roles", backref="person", uselist=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    firstname = db.Column(db.String(500),nullable=True)
    lastname = db.Column(db.String(500),nullable=True)
    verification = db.Column(db.String(20), nullable=True)
    organization = db.Column(db.String(15), nullable=True)

    def __repr__(self):
    	return f"User('{self.id}','{self.email}','{self.profile_pic}','{self.role_id}')"