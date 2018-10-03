from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import base, engine


class User(base):
  __tablename__ = 'users'

  tablename = 'users'
  id = Column('id', Integer, primary_key = True)
  user_name = Column('comic_name', String(200))
  age = Column('age', Integer)


def __init__(self, user_name=None, age=None):
  self.user_name = user_name
  self.age = age

def __repr__(self):
  return '<user_name %r>' % (self.user_name)
