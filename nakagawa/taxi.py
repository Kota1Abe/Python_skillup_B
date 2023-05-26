import math
import sys
args = sys.argv

#タクシー初乗り1500mまで630円
#344mごとに+98円

ADDIIONAL_DIS = 344
distance = int(args[1])
sum = 630

if distance > 1500:
  over = distance - 1500
  over_amount = 98 * math.ceil(over / ADDIIONAL_DIS)
  sum += over_amount

print(sum, end="")
