
sms_key = "24be6ffdbdc18"

BASE = "mysql+pymysql://user:password@192.168.0.{0}:3306/db"
READ_DATABASE = BASE.format(250)
WRITE_DATABASE = BASE.format(251)

class Config:
    SECRET_KEY = "miyao"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@localhost:3306/dbname" #WRITE_DATABASE
    

class DeveploeConfig(Config):
    DEBUG = True
    

class ReleaseConfig(Config):
    DEBUG=False

config = {
    'develop':DeveploeConfig,
    'release':ReleaseConfig
}
