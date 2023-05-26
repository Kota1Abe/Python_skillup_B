import sys 
# 소수인지 판정 
num = int(sys.argv[1])

def hantei(num):
   
    if num >= 1000:
        print("1000以上は判定できません",end="")
    
    else:    
       if num >= 1:
            
            for i in range(2,num):
                if num % i==0:
                    print("not",end="")
                    break
                print("Prime",end="")
                break
hantei(num)

# import sys 
# # 소수인지 판정 
# num = int(sys.argv[1])

# def hantei(num):
#     if num >= 1000:
#         print("1000以上は判定できません",end="")
#     elif num > 1:
        
#             for i in range(2,num):
#                 if num % i:
#                     is_prime = False
#                     break
#             if is_prime:
#                  print("prime",end="")
#                  num = 0
# hantei(num)
        
        
# hantei(num)

        # if num % 2 == 0 or num  :
        #     print("prime")
        # else : 
        #  print("not",end="")

