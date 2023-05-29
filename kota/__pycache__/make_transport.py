import sys
from sqlalchemy import Column,String,Numeric,Integer
from database import Base
from database import ENGINE

class Make_transport(Base):
    __tablename__='transport'
    data=Column("data",Integer,primary_key=True) #駅番号
    seq=Column("seq",String(20)) #駅名
    kilo=Column("kilo",Numeric(6,2)) #東京駅からの距離 (６桁で小数点以下２桁)

def main(args):

    Base.metadata.create_all(bind=ENGINE)
    
if __name__=="__main__":
    main(sys.argv)
    