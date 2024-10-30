from api.extensions import db
from sqlalchemy import (
  Column, String, UUID, ForeignKey
)
from uuid import uuid4


class User(db.Model):
  __tablename__ = 'users'
  id = Column(UUID(as_uuid=True),default=uuid4, primary_key=True, nullable=False)
  username = Column(String, nullable=False, unique=True)
  email = Column(String, nullable=False, unique=True)
  password_hash = Column(String, nullable=False)
