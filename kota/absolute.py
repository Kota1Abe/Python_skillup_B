import sys
args = sys.argv

num=int(args[1])

if num <0:
    absolute_value= -1*(num)

else:
    absolute_value=num

print(f"{num} {absolute_value}",end="")