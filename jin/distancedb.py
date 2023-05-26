import sys
from sqlalchemy import Column , String , Date , Integer, VARCHAR,DECIMAL
from stations import Stations
from database2 import session
# stations 파일의 Stations 클래스를 임포트 

import sys 



num_loop,num, eki,kilo = sys.argv[1:]
for i in num_loop: # 루프를 돌려서, 데이터를 
    # 여러개 삽입해볼 생각 
    stations = Stations(
        # stations 파일안의 Stations 클래스에 넣는다
        st_seq = int(num) ,
        st_name = eki ,
        st_kilo = int(kilo) 
    )
    session.add(stations)
    session.commit()
