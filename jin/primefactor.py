
# 소인수 분해 # 
import sys 

num = int(sys.argv[1])


# 소인수 분해는 2부터 시작해서, 전체의 수까지 나누어봐야한다. 

# li =[]
# for i in range(2,num,1): # range함수에서는 특정 조건이 발생하였을 때, 값을 초기화 하지못함. 
#     if num % i == 0:
#         li.append(i)
#         num = num / i # num = 17, i=18 
        

# print(li) 
i =2 
li = []
while i < num:
    if num % i == 0:
        li.append(i)
        num = num/i 
        i=1
    else:
        i+=1  
        print(i)
print(li)