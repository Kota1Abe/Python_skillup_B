import sys
args = sys.argv

num=int(args[1])

if 0<=num <= 1500:
    fare=630

elif num>1500:
    diff=num-1500
    add_fare=(diff+344-1)//344*98
    fare=630+add_fare

print(fare,end="")
