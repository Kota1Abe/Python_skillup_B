import sys
args = sys.argv
import os
import qrcode

#読み込むテキストファイルを指定
file_name = args[1]

with open(file_name, mode= "r", encoding="utf8") as f:
    idx = 0 #ファイル名は連番
    for url in f:
        idx += 1
        path = os.path.join("output", f'{idx}.png')
        img = qrcode.make(url)
        img.save(path)

    