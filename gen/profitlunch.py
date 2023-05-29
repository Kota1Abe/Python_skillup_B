# 引数のライブラリをimport
import sys
args = sys.argv
import math

chiken = int(args[1])
curry = int(args[2])

chiken_cost = 0.323
curry_cost = 0.284

chiken_sum = (chiken * 760)
curry_sum = (curry * 850)

Earnings = (chiken * 760) + (curry * 850)

chiken_sale = round(chiken_sum * chiken_cost)
curry_sale = round(curry_sum * curry_cost)

cost =  chiken_sale + curry_sale
profit = Earnings - cost

print("売上高：" + str(Earnings) + "、原価：" + str(cost) + "、粗利：" + str(profit), end="")