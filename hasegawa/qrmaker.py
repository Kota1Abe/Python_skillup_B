# # 引数モジュールをimport
import sys
args = sys.argv

# QR作成モジュールをimport
import qrcode

# モジュール「os」のimport
import os

# 第二引数を読み込むファイル用の変数に代入
input_path = args[1]

# 連番用変数の初期化
num = 0

# ファイル読み込み処理
with open(input_path, mode= "r", encoding="utf-8") as qrmake_file:
    # テキストファイルの行数文繰り返す処理
    for line in enumerate(qrmake_file):
        # 連番処理
        num += 1
        
        path = os.path.join("output", f"{num}.png")
        # 一行分のurlを読み込みqrコードを作る
        img = qrcode.make(line)
        # あらかじめ指定したpathに連番.pngを保存する
        img.save(path)