#モジュールをインポート
import sys
args = sys.argv
from database import session
from transtable import Transport
from datetime import datetime

#引数に設定した値を表に登録する関数を作成
def insert_transport():
    date = args[1]
    departure = args[2]
    arrival = args[3]
    via = args[4]
    amount = int(args[5])

    #date型に変換
    dt = datetime.strptime(date, "%Y%m%d")

    #連番するためにテーブルの行をcount
    seq = session.query(Transport).count()
    date = dt

    #表に登録
    transport = Transport(
        date = date,
        seq = seq + 1,
        departure = departure,
        arrival = arrival,
        via = via,
        amount = amount
    )

#errorの表示
    try:
        session.add(transport)
        session.commit()
        print("交通費精算テーブルを登録しました")
    except:
        print("交通費精算テーブルを登録できませんでした")

#関数の呼びだし
insert_transport()