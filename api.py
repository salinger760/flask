from sqlalchemy import *
from sqlalchemy.orm import *

import sqlalchemy as sa
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, join, func

from flask import Flask, jsonify, abort, make_response, request
from flask_sqlalchemy import SQLAlchemy
import random
import json


def random_string(length, seq='0123456789abcdefghijklmnopopqrstuvwxyz'):
  sr = random.SystemRandom()
  return ''.join([sr.choice(seq) for i in range(length)])

api = Flask(__name__)

config = {
  "user": "maria",
  "password": "maria",
  "host": "127.0.0.1",
  "port": 3306,
  "database": "wikitest"
}

dsn_fmt = "mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s?charset=utf8"
dsn = dsn_fmt % config

api.config['SQLALCHEMY_DATABASE_URI'] = dsn

db = SQLAlchemy(api)

#engine = create_engine(dsn, echo=True)
#metadata = MetaData(bind=engine)
#Base = declarative_base()

class Page(Base):
  __tablename__ = "pages"

  id   = Column(Integer, primary_key=True)
  url  = Column(String(255), unique=True, nullable=False)
  html = Column(Text(4096) , nullable=True)
  http_status = Column(Integer, default=0, nullable=True )
  status = Column(Integer, default=0, nullable=True )

  def is_not_found():
    return  self.http_status == 404


@api.route('/user/<string:UserId>', methods=['GET'])
def get_user(userId):
  try:
    user = Page.


Base.metadata.create_all(engine)
