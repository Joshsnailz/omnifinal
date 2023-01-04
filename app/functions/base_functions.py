from functools import wraps
from flask import current_app, request, redirect, url_for,flash
from flask_login import current_user, login_user
from app.models.user import User, Roles
from passlib.hash import pbkdf2_sha256
from app import db

def requires_role(role):
    def decorator(function):
        @wraps(function)
        def inner_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash(f'You are unauthorized to access that page','danger')
                return redirect(url_for('auth.signin', next=request.url))
                
            if current_user.role.role_shortcut != role:
                flash(f'Only a { role}  is allowed to access that page!! ','danger')
                return redirect(url_for(current_user.role.role_shortcut+'.index'))

            return function(*args, **kwargs)

        return inner_function
    return decorator



def authenticate_user(email, password):
    data_dict = dict(message='', status='failed', data=None)
    with current_app.app_context():
        user = User.query.filter_by(email=email).first()
        if user and pbkdf2_sha256.verify(password, user.password):
            if user.verification != 'verified':
                data_dict['message'] = 'Your account has not yet been verified, Kindly check your email and follow the instructions!!'
            elif user.role_id ==9:
                data_dict['message'] = 'Your account no longer exists, contact admin for further inquiries!'
            else:
                login_user(user)
                data_dict['status'] = 'success'
                data_dict['data'] = user.role.role_shortcut
        else:
            data_dict['message'] = 'Incorrect login credentials!'

    return data_dict


def get_role_id(rolename):
    with current_app.app_context():
        role = Roles.query.filter_by(role_shortcut=rolename).first()
        return role 

def validate_registration(email):
    with current_app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            user.verification = 'verified'
            db.session.add(user)
            db.session.commit()
        pass 







