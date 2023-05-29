import sys
args = sys.argv
from database import session
from make_transport import Transport_make
from datetime import datetime
import os

path=os.path.join("..","output","output.txt")

with open(path,mode="w",encoding="utf-8") as output:

    datalist=session.query(Transport_make.data).all()
    
    for i in range(len(datalist)):

        date_type=datalist[i][0]
        date = date_type.year * 10000 + date_type.month * 100 + date_type.day
        #print(int_date)

        seqlist=session.query(Transport_make.seq).all()
        seq=seqlist[i][0]

        departurelist=session.query(Transport_make.departure).all()
        departure=departurelist[i][0]

        arrivallist=session.query(Transport_make.arrival).all()
        arrival=arrivallist[i][0]

        vialist=session.query(Transport_make.via).all()
        via=vialist[i][0]

        amountlist=session.query(Transport_make.amount).all()
        amount=amountlist[i][0]

        output.write(f"\"{date}\",\"{seq}\",\"{departure}\",\"{arrival}\",\"{via}\",\"{amount}\"\n")
