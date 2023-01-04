from .base.home import home_blueprint
from .base.basic_user_action import basic_blueprint
from .candidate.candidate import candidate_blueprint
from .jobs.home import jobs_blueprint

blueprints = [
    dict(blueprint=home_blueprint, url_prefix='/'),
    dict(blueprint=basic_blueprint, url_prefix='/basic'),
    dict(blueprint=candidate_blueprint, url_prefix='/candidate'),
    dict(blueprint=jobs_blueprint,url_prefix='/jobs')
]