# 引数のライブラリをimport
import sys
args = sys.argv
import math

chiken = int(args[1])
curry = int(args[2])

Earnings = (chiken * 760) + (curry * 850)

print(Earnings)