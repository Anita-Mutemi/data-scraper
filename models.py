from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    linkedin_id = Column(String, nullable=False, unique=True)

    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    post_id = Column(String, nullable=False, unique=True)
    user_id = Column(String, ForeignKey('users.linkedin_id'), nullable=False)

    user = relationship('User', back_populates='posts')
    likers = relationship('Liker', back_populates='post')

class Liker(Base):
    __tablename__ = 'likers'

    id = Column(Integer, primary_key=True)
    liker_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    title = Column(String)
    post_id = Column(String, ForeignKey('posts.post_id'), nullable=False)

    post = relationship('Post', back_populates='likers')