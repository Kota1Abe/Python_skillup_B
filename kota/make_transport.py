import sys
from sqlalchemy import Column,String,Integer,Date
from database import Base
from database import ENGINE

class Transport_make(Base):
    __tablename__='Transport'
    data=Column("data",Date,primary_key=True) #利用日
    seq=Column("seq",Integer,primary_key=True) #連番
    departure=Column("departure",String(20)) #出発地
    arrival=Column("arrival",String(20)) #到着地
    via=Column("via",String(40)) #経由/利用交通機関
    amount=Column("amount",Integer) #金額
    
def main(args):

    Base.metadata.create_all(bind=ENGINE)

if __name__=="__main__":
    main(sys.argv)
    