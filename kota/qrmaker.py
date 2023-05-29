import qrcode
import os

count=1
path_list=os.path.join("./","qr_text","qrlist.txt")

with open(path_list,mode="r",encoding="utf-8") as file:
    for line in file:
        name=f"{count}.png"
        path_save=os.path.join("..","output",name)
        img=qrcode.make(line)
        img.save(path_save)
        count +=1
