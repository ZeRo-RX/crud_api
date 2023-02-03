from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.expression import text
from .db_connection import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    content = Column(String, index=True, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_time = Column(DateTime(timezone=True), nullable=False, default=func.now())


# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True, nullable=False)
#     mail = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     created_time = Column(DateTime(timezone=True), nullable=False, default=func.now())


