import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))   

class Config:
   SECRET_KEY = os.environ.get("SECRET_KEY") or "gombao33"
     
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), '..', 'db.sqlite')
   SQLALCHEMY_TRACK_MODIFICATIONS = False