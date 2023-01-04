from flask import Blueprint, render_template, flash
from app.models.jobs import Job
import datetime
from app import db
from app.functions.job_functions import query_job_by_department



jobs_blueprint = Blueprint('jobs', __name__)


@jobs_blueprint.route('jobs/<key>', methods=['GET','POST'])
def home(key):
    jobs = query_job_by_department(key)
    print("This is what the key returned", jobs)
    return "This is the home of jobs"