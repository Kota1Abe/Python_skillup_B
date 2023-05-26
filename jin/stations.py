import sys
from sqlalchemy import Column , String , Date , Integer, VARCHAR,DECIMAL
from database2 import Base
from database2 import ENGINE 
# 새롭게 만든 database2에서 불러옴 
class Stations(Base):
    __tablename__ = "stations"
    st_seq = Column("seq", Integer,primary_key = True)
    st_name = Column("name",VARCHAR(20))
    st_kilo = Column("kilo",DECIMAL)
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if  __name__ == "__main__":
    main(sys.argv)  