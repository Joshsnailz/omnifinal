from flask import Flask, session
from flask.sessions import SecureCookieSessionInterface
from app.config.basic_configs import BasicConfig
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import datetime
import os 
from flask_ckeditor import CKEditor
from flask_migrate import Migrate




mail = Mail()
db = SQLAlchemy()
s = URLSafeTimedSerializer('Thisisimyserialsierrsathatsiwloduses')
csrf = CSRFProtect()
ckeditor = CKEditor()
login_manager = LoginManager()
migrate = Migrate()


#initialization of all things 
def create_app():
   app = Flask(__name__, template_folder='./templates')
   app.config.from_object(BasicConfig)
   app.config.update(SESSION_COOKIE_NAME = 'my_test_cookie')
   app.config.update(SESSION_COOKIE_SAMESITE  = 'None')
   app.config.update(WTF_CSRF_SECRET_KEY ='THISdhrfhgdsjnfkdnnxndhdhdbdhd')
   app.config.update(WTF_CSRF_ENABLED = False)


   mail.init_app(app)
   db.init_app(app)
   csrf.init_app(app)
   login_manager.init_app(app)
   ckeditor.init_app(app)
   migrate.init_app(app,db)

   session_cookie = SecureCookieSessionInterface().get_signing_serializer(app)
   login_manager.login_view = 'auth.signin'
   login_manager.refresh_view ='auth.signin'
   login_manager.needs_refresh_message = (u'Session timeout, please log in again')
   login_manager.needs_refresh_message_category = 'danger'


   @app.before_request
   def before_request():
      session.permanent = True
      app.permanent_session_lifetime = datetime.timedelta(minutes=10)


   @app.after_request
   def cookies(response):
      same_cookie = session_cookie.dumps(dict(session))
      response.headers.add("Set-Cookie", f"my_cookie={same_cookie}; Secure; HttpOnly; SameSite=None; Path=/;")
      return response


   from app.models.user import User
   @login_manager.user_loader
   def load_user(user_id):
        return User.query.get(int(user_id))

   
   #registering all my blueprints 
   from app.views import blueprints
   for blueprint in blueprints:
      url_prefix = blueprint['url_prefix']
      if not url_prefix:
         url_prefix = '/' + blueprint['blueprint'].name
      app.register_blueprint(blueprint['blueprint'],url_prefix=url_prefix)



   return app 

   


