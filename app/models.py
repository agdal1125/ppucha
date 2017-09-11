from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
  __tablename__ = 'moms'
  name = Column(String(3), primary_key = True)
  birthday = Column(Integer, unique = False)
  lucky = Column(Integer, unique = False)
  barcode = Column(Integer, unique = True)

  def __init__(self, name = None, birthday = None, lucky = None, barcode = None):
    self.name = name
    self.birthday = birthday
    self.lucky = lucky
    self.barcode = barcode

  def __repr__(self):
    return '<User %r>' % (self.name)


