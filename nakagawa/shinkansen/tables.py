import sys
from sqlalchemy import Column,String, Numeric, Integer
from database import Base
from database import ENGINE

class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key=True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6,2))

def main(args):
    Base.metadata.create_all(bind = ENGINE)

if __name__ == '__main__':
    main(sys.argv)

