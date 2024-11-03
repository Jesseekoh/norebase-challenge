import os
from cachelib.file import FileSystemCache
class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')
  SESSION_TYPE = os.environ.get('SESSION_TYPE', 'cachelib')
  SESSION_COOKIE_HTTPONLY= os.environ.get('SESSION_COOKIE_HTTPONLY', 'True')
  SESSION_COOKIE_SECURE= os.environ.get('SESSION_COOKIE_SECURE', 'True')
  SESSION_PERMANENT = os.environ.get('SESSION_PERMANENT', 'False')
  SESSION_SERIALIZATION_FORMAT=os.environ.get('SESSION_SERIALIZATION_FORMAT', 'json')
  SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress a warning from SQLAlchemy
  SESSION_CACHELIB = FileSystemCache(threshold=500, cache_dir=f"{os.path.dirname(__file__)}/sessions")
