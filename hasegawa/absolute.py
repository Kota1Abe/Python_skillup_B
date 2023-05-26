# 引数のライブラリをimport
import sys
args = sys.argv

# 第二引数をnumに代入
num = int(args[1])
# numの絶対値をabs_numに代入
abs_num = abs(num)

print(str(num)+" "+str(abs_num),end="")