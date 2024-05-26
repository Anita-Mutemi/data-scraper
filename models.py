from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Postowner(Base):
    __tablename__ = 'postsowners'

    id = Column(Integer, primary_key=True)
    post_id = Column(String, nullable=False, unique=True)
    user_id = Column(String, nullable=False, unique=True)

    likers = relationship('Liker', back_populates='post')

class Liker(Base):
    __tablename__ = 'likers'

    id = Column(Integer, primary_key=True)
    liker_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    post_id = Column(String, ForeignKey('Postowner.post_id'), nullable=False, unique=True)

    post = relationship('Postowner', back_populates='likers')