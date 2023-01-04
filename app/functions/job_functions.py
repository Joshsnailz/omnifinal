from functools import wraps
from flask import current_app, request, redirect, url_for,flash
from flask_login import current_user, login_user
from app.models.user import User, Roles
from passlib.hash import pbkdf2_sha256
from app import db
from app.models.jobs import Job

def query_job_by_department(department):
    jobs = Job.query.filter(Job.status=="Published", Job.department==department).all()
    return jobs 

    

