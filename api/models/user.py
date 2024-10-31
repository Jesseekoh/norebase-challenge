from api.extensions import db
from sqlalchemy import (
  Column, String, UUID, ForeignKey, Table
)
from sqlalchemy.orm import relationship
from uuid import uuid4


class User(db.Model):
  __tablename__ = 'users'
  id = Column(UUID(as_uuid=True),default=uuid4, primary_key=True, nullable=False)
  username = Column(String, nullable=False, unique=True)
  email = Column(String, nullable=False, unique=True)
  password_hash = Column(String, nullable=False)
  liked_articles = relationship('Article', secondary='user_article_likes', back_populates='liked_by_users')
  

user_article_likes = Table('user_article_likes', db.Model.metadata, 
  Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'),               
      primary_key=True),
  Column('article_id', UUID(as_uuid=True), ForeignKey('articles.id'), 
      primary_key=True)
)
