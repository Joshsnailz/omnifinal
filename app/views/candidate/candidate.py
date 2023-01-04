from flask import Blueprint, render_template

candidate_blueprint = Blueprint('candidate', __name__)

@candidate_blueprint.route('/')
def index():
    return render_template('candidate/index.html', title='Home')

