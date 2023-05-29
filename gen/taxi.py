# 引数のライブラリをimport
import sys
args = sys.argv
import math

distance = int(args[1])

add = distance - 1500

add_num = math.ceil(add / 344)


if distance >= 1501 :
    sum = (add_num * 98 + 630)
    print(sum, end="")
else:
    print(630, end="")
