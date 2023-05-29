import sys
from sqlalchemy import Column , String , Date , Integer, VARCHAR,DECIMAL
from stations import Stations
from database2 import session
# stations 파일의 Stations 클래스를 임포트 

import sys 



eki,eki2 = sys.argv[1:]
# for i in range(num_loop): # 루프를 돌려서, 데이터를 
#     # 여러개 삽입해볼 생각 

# sys로 입력을 받기 때문에, 한번씩 돌려서, 입력 값을 받는다. 

dt = session.query(Stations).filter_by(st_name=eki).first()
dt2 = session.query(Stations).filter_by(st_name=eki2).first()
# 값을 받을 변수= session.quert ( 클래스 명 ).filter_by(클래스 안의 변수와 비교할 값)
#.first() 하나의 값만 들고오기 
print(abs(dt.st_kilo - dt2.st_kilo))

# stations = Stations(
#         # stations 파일안의 Stations 클래스에 넣는다
#     st_seq = int(num) ,
#     st_name = eki ,
#     st_kilo = kilo
#     )
# session.add(stations)
# session.commit()