import sys 

n = int(sys.argv[1])

distance = int(sys.argv[1])
fee = 630
if distance <= 1500:
    print(f"{fee}",end="")
else : 
    fee = 728
    res = (distance - 1500)
  
    fee = fee + (int(res/344) * 98)  
    print(round(fee,),end="")