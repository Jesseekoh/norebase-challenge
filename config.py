import os


class Config:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///articles.db'
  SESSION_TYPE = os.environ.get('SESSION_TYPE')
