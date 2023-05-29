import sys
args = sys.argv
from database import session
from tables import Transport

file_name = args[1]

#交通費精算テーブルからデータを取得
data = session.query(Transport).order_by(Transport.seq).all()

#指定したファイルに、取得したデータを書き込み、outputフォルダに格納
with open(f'/home/matcha-23training/Python_skillup_B/nakagawa/output/{file_name}', mode="w", encoding="utf-8") as f:
  for r in data:
    dt = r.date.strftime("%Y%m%d")
    f.write(f'{dt, r.seq, r.departure, r.arrival, r.via, r.amount}\n')
    
