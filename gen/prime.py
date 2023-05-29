# 引数のライブラリをimport
import sys
args = sys.argv

#引数を変数に代入
num = int(args[1])

#素数判定
def isprime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

#1000以上は抜け出し判定を出力
if num >=1000:
    print("1000以上は判定できません",end="")

else:
    if isprime(num):
        print("Prime",end="")
    else:
        print("not",end="")