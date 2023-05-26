li = ["Kurita","Tanaka","Kaneda",
      "Noda","Koyama","Adachi","Kuriyama","Ohyama","Kishida"]

import sys

li2=[]


for i in range(len(li)):
    if i % 2==1:
        li2.append(li[i])

print(li2,end="")