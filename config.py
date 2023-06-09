import os

class Config:
    SECRET_KEY = 'tu_clave_secreta'
    #FLASK_APP='app:create_app("config.ProdConfig")' 
    #Error: Detected factory 'create_app' in module 'app',
    #but could not call it without arguments. Use 'app:create_app("config.DevConfig")' 
    #to specify arguments.

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #FLASK_ENV= "development"
    #FLASK_DEBUG= 1 
    #DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #FLASK_ENV = "production"
    #DEBUG = False
    #FLASK_DEBUG= 0
    