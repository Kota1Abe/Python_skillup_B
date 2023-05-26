# 가라아게 , 원가률 
#  750 
# 카레 셋 , 원가률 
# 850 

# 원가률은 이익률의 반대 

import sys 
food1 = int(sys.argv[1])
food2 = int(sys.argv[2])
chi = 760
kare = 850
money = food1 * chi + food2 * kare

genka = chi*0.323*food1 + kare*0.284*food2
print(f"売上高：{round(money)}、 原価：{round(genka)}、 粗利：{round(money-genka)}",end="")

