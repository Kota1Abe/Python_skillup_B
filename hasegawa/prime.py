# 引数のモジュールをimport
import sys
args = sys.argv

import math

# 第二引数をinput_numに代入
number = int(args[1])

# 1000以上の場合は素数判定停止
if number >= 1000:
    print("1000以上は判定できません", end ="")

else:
    flag = 0

    # 2より小さい場合素数ではないためflagに1を代入
    if number < 2:
        flag = 1
    # 2の場合素数なためflagに0を代入
    elif number == 2:
        flag = 0
        
    # 2で割り切れる場合素数ではないためflagに1を代入
    elif number % 2 == 0:
        flag = 1
    i = 3

    while number > i:
        if number % i == 0:
            # 3以上の奇数で割り切れる場合素数ではないためflagに1を代入
            flag = 1
            break
        i += 2
# 判定結果出力
    if flag == 0:
        print("Prime", end="")
    else:
        print("not",end ="")


            