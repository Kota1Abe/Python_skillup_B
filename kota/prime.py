import sys
args = sys.argv
num=int(args[1])

#素数判定
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if num >=1000:
    print("1000以上は判定できません",end="")

else:
    if is_prime(num):
        print("prime",end="")
    else:
        print("not",end="")