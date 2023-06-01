# モジュールをインポート
import sys
args = sys.argv
from database import session
from transtable import Transport
from datetime import datetime
import os

#引数を変数に代入
file = args[1]

# データの抽出
data = session.query(Transport).order_by(Transport.seq).all()

# テキストデータの作成/格納
with open(f'output/{file}', "w", encoding="utf-8") as f:
    #ファイルに書き込む
    for row in data:
        dt = row.date.strftime("%Y%m%d")
        f.write(f'{dt, row.seq, row.departure, row.arrival, row.via, row.amount}\n')