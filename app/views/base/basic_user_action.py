from flask import Blueprint, render_template , redirect, url_for, request, flash, session, current_app, jsonify
from itsdangerous import SignatureExpired, BadTimeSignature
from app.models.user import User, Roles
from app.functions.base_functions import authenticate_user, get_role_id, validate_registration
from app.forms.base_forms import LoginForm
from passlib.hash import pbkdf2_sha256
from app import db
from flask_login import login_user,current_user,logout_user,login_required
import datetime


basic_blueprint = Blueprint('basic',__name__ )






@basic_blueprint.route('/signin', methods=['GET','POST'])
def signin():
    form = LoginForm()
    print("We have come heres")
    if not current_user.is_authenticated :
        if form.validate_on_submit():
            print("The form has been submitted and the csrf token ", form.email.data)
            is_auth = authenticate_user(form.email.data, form.password.data)
            if is_auth['status'] == 'success':
                next_url = request.args.get('next', '/' + is_auth['data'])
                return redirect(next_url)
            else:
                flash(is_auth['message'], 'danger')
                
    return render_template('base/pages-sign-in.html', form=form ,title='Sign in')

@basic_blueprint.route('/signup')
def signup():
    return render_template('base/pages-sign-up.html', title='Sign Up Now!!')

