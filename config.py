import os
from flask_appbuilder.security.manager import AUTH_DB

sms_key = "24be6ffdbdc18"

_user = os.getenv('mysql_user')
_passwd = os.getenv('mysql_passwd')
_host = os.getenv('mysql_host')
_db = os.getenv('mysql_db')
print('use env variables')
BASE = "mysql+pymysql://"+_user+":"+_passwd+"@"+_host+":3306/"+_db
READ_DATABASE = BASE
WRITE_DATABASE = BASE


class Config:
    SECRET_KEY = "miyao"
    SQLALCHEMY_DATABASE_URI = WRITE_DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CSRF_ENABLED = True
    APP_NAME = "I.B.G"  
    AUTH_TYPE = AUTH_DB
    BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_FOLDER = 'translations'
    LANGUAGES = {
    'en': {'flag':'gb', 'name':'English'},
    'pt': {'flag':'pt', 'name':'Portuguese'},
    'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
    'es': {'flag':'es', 'name':'Spanish'},
    'de': {'flag':'de', 'name':'German'},
    'zh': {'flag':'cn', 'name':'Chinese'},
    'ru': {'flag':'ru', 'name':'Russian'},
    'pl': {'flag':'pl', 'name':'Polish'}}
    APP_THEME = "bootstrap-theme.css"
    app_key = u''
    master_secret = u''


class DeveploeConfig(Config):
    DEBUG = True


class ReleaseConfig(Config):
    DEBUG = False


config = {
    'develop': DeveploeConfig,
    'release': ReleaseConfig
}

