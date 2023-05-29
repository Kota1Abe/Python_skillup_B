import sys
args = sys.argv
from database import session
from tables import Transport
from datetime import datetime

#引数で設定した値を交通費精算テーブルに登録する
def insert_transport():
  date = args[1]
  departure = args[2]
  arrival = args[3]
  via = args[4]
  amount = int(args[5])

  dt = datetime.strptime(date, "%Y%m%d")
  seq = session.query(Transport).count()
  date = dt.date()
  transport = Transport(
      date = date,
      seq = seq + 1,
      departure = departure,
      arrival = arrival,
      via = via,
      amount = amount
  )
  try:
    session.add(transport)
    session.commit()
    print("交通費精算テーブルにデータを登録しました")
  except:
    print("交通費精算テーブルにデータを登録できませんでした")

insert_transport()