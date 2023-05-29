import sys
from sqlalchemy import Column,String, Numeric, Integer,Date
from database import Base
from database import ENGINE

#
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key=True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6,2))

class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key=True)
    seq = Column('seq', Integer, primary_key=True)
    departure = Column('departure', String(20))
    arrival = Column('arrival', String(20))
    via = Column('via', String(40))
    amount = Column('amount', Integer)

def main(args):
    Base.metadata.create_all(bind = ENGINE)

if __name__ == '__main__':
    main(sys.argv)

