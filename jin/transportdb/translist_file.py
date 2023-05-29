import sys
from sqlalchemy import Column , String , Date , Integer, VARCHAR,DECIMAL
from transport import Transport
from transportdb import session

result = session.query(Transport).filter_by().all()

out_file = open('output.txt',mode='w')

# print(result) # 주소 값 
for row in result:
    out_file.write(f'{row.tr_date},{row.tr_seq},{row.tr_departure},{row.tr_arrival},{row.tr_via},{row.tr_amount}\n')
    

out_file.close()

### 파일 읽기 ### 

fl = open('output.txt','r')

print(fl.read())

fl.close()

