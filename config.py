#from dotenv import load_dotenv
import os
#load_dotenv()

class Config:
    DEBUG = False
    SECRET_KEY = 'tu_clave_secreta'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass