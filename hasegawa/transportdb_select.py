# # 引数モジュールをimport
import sys
args = sys.argv

name_txt = str(args[1])

# データベース接続
from database import session

# テーブル定義
from transportdb_make import Transport

# ファイル書き込み処理
with open("/home/matcha-23training/Python_skillup_B/hasegawa/output/"+name_txt+"", mode="w", encoding="utf-8") as trans_expense_file:
    for row in session.query(Transport.date, Transport.seq, Transport.departure, Transport.arrival, Transport.via, Transport.amount).all():
        dt = row.date.strftime("%Y%m%d")
        trans_expense_file.write('"'+str(dt)+'"'+',"'+str(row[1])+'"'+',"'+str(row[2])+'"'+',"'+str(row[3])+'"'+',"'+str(row[4])+'"'+',"'+str(row[5])+'"'+'\n')