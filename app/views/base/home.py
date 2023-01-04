from flask import Blueprint, render_template, flash
from app.models.jobs import Job
import datetime
from app import db



home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET','POST'])
def index():
    try:
        #jobs = Job.query.filter(Job.status=="Published").all()
        jobs = Job.query.all()
        date_today = datetime.datetime.now()
        if jobs:
            for job in jobs:
                if job.due_date < date_today:
                    job.status ="Previous"
                    db.session.add(job)
                    db.session.commit()
    except Exception as e:
        flash(f'There has been an error --> {e}','danger')
        
    hr_job_count = Job.query.filter(Job.status=="Published", Job.department=="Human Resource").count()
    back_office_job_count = Job.query.filter(Job.status=="Published", Job.department=="Back Office").count()
    is_job_count = Job.query.filter(Job.status=="Published", Job.department=="Information Systems").count()
    internship_roles_count = Job.query.filter(Job.status=="Published", Job.department=="Internships").count()
    call_centre_job_counts = Job.query.filter(Job.status=="Published", Job.department=="Call Centre").count()
    reporting_jobs_count = Job.query.filter(Job.status=="Published", Job.department=="Reporting").count() 


    return render_template('base/index.html', title='Home', jobs=jobs, hr_job_count=hr_job_count,back_office_job_count=back_office_job_count,is_job_count=is_job_count,internship_roles_count=internship_roles_count,call_centre_job_counts=call_centre_job_counts,reporting_jobs_count=reporting_jobs_count)

