import sys
from sqlalchemy import Column , String , Date , Integer, VARCHAR,DECIMAL,DATE 
from transportdb import Base
from transportdb import ENGINE 
# 새롭게 만든 transportdb에서 불러옴 
class Transport(Base):
    __tablename__ = "transport"
    tr_date = Column("date", Date,primary_key = True) #이용일 
    tr_seq = Column("seq",Integer) # 순번 
    tr_departure = Column("departure",VARCHAR(20)) # 출발지 
    tr_arrival = Column("arrival",VARCHAR(20)) # 도착지 
    tr_via = Column("via",VARCHAR(40)) # 경유 , 이용교통 기관 
    tr_amount = Column("amount",Integer) # 금액 
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if  __name__ == "__main__":
    main(sys.argv)  