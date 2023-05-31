# 引数モジュールをimport

import sys
args = sys.argv


# 日付のモジュールをimport
ins_date = args[1]
from datetime import datetime
ins_dt = datetime.strptime(ins_date,"%Y%m%d")

# print(ins_dt)

# それぞれの引数を指定された項目の変数に代入
ins_seq = int(args[2])
ins_dep = str(args[3])
ins_arr = str(args[4])
ins_via = str(args[5])
ins_amo = int(args[6])

from database import session

# Transportクラスをimport

from transportdb_make import Transport

# 例外処理
try:

    transport = Transport(
        date = ins_dt,
        seq = ins_seq,
        departure = ins_dep,
        arrival = ins_arr,
        via = ins_via,
        amount = ins_amo
        )

    # Insert処理
    session.add(transport)

    # コミット
    session.commit()
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")