import sys 

food1 = int(sys.argv[1])
food2 = int(sys.argv[2])
chi = 760
kare = 850
money = food1 * chi + food2 * kare
print(money,end="")