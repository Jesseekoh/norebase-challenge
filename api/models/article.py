from sqlalchemy import (
  Column, Integer, String, UUID, ForeignKey
)
from sqlalchemy.orm import relationship
from uuid import uuid4
from api.extensions import db

class Article(db.Model):
  __tablename__ = 'articles'

  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  like_count = Column(Integer, default=0)
  liked_by_users = relationship('User', secondary='user_article_likes', back_populates='liked_articles')
