import sys
from sqlalchemy import Column , String , Date , Integer, VARCHAR,DECIMAL
from transport import Transport
from transportdb import session
# stations 파일의 Stations 클래스를 임포트 

import sys 

## 데이터 입력 ## 

# to_date,seq,eki,eki2, line, money = sys.argv[1:]
# for i in range(num_loop): # 루프를 돌려서, 데이터를 
####



## 데이터 등록 ## 
# transport = Transport(
#         # stations 파일안의 Stations 클래스에 넣는다
#     tr_date = to_date , # 기본키로 설정되어있기 때문에, 똑같은 날짜를 추가할 수 없다. 
#     tr_seq = int(seq) ,
#     tr_departure = eki,
#     tr_arrival = eki2,
#     tr_via = line,
#     tr_amount = int(money)
#     )
# session.add(transport)
# session.commit()

# ## 

# # fr = open('translist.txt',"r")

# # text = fr.read()

# dt = session.query(Transport).filter_by().all()

# print(dt)

## 파일 출력 저장 ## 

out_file = open('translist.py',"r")

print(out_file)

out_file.close()

# out_file.write('translist.py','r')