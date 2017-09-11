from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://jaekeun:1125@localhost:5432/ppucha')

db_session = scoped_session(sessionmaker(autocomit = False,
                                         autoflush = False,
                                         bind = engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import models
  Base.metadata.create_all(bind=engine)


