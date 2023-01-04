import os 
import datetime 

basedir = os.path.abspath(os.path.dirname(__file__))

class BasicConfig(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkeyisehere'
    FILE_UPLOAD_DIRECTORY = os.path.join(basedir,'static','uploads')
    ALLOWED_FILE_EXTENSIONS = ['docx','pdf','doc','jpg','jpeg','png']
    SESSION_COOKIE_SAMESITE='None'

    #database configurations
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #DATABASE_URL = 'postgres+psycopg2://postgres:password@host/database'
    # or 'postgresql+psycopg2://postgres:omn5114@192.168.55.117/omnisprint'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:omn5114@localhost/omnisprint'
    DATABASE_URL = 'postgresql+psycopg2://postgres:omn5114@192.168.55.115/omnisprint'
    SQLALCHEMY_TRACK_MODIFICATION = False
    MAX_CONTENT_LENGTH = 3*1024*1024 

    #email server configurations 
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = True
    MAIL_USERNAME = 'admin@ommicontact.biz'
    MAIL_PASSWORD = '#pass123'
    MAIL_SUPPRESS_SEND = True
    #Google Captcha 

    