import os


class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')
  SESSION_TYPE = os.environ.get('SESSION_TYPE', 'redis')
  SESSION_COOKIE_HTTPONLY= os.environ.get('SESSION_COOKIE_HTTPONLY', 'True')
  SESSION_COOKIE_SECURE= os.environ.get('SESSION_COOKIE_SECURE', 'True')
  SESSION_PERMANENT = os.environ.get('SESSION_PERMANENT', 'False')
  SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress a warning from SQLAlchemy
