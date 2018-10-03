from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

config = {
  "user": "maria",
  "password": "maria",
  "host": "127.0.0.1",
  "port": 3306,
  "database": "wikitest"
}

dsn_fmt = "mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s?charset=utf8"
dsn = dsn_fmt % config


engine = create_engine(
  dsn,
  encoding = 'utf-8',
  echo = True
)

session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

base = declarative_base()
base.query = session.query_property()
