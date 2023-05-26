# 引数のモジュールをimport
import sys
args = sys.argv

# 第二引数を唐揚げ定食の一日注文数orders_friedchicken_setに代入
orders_friedchicken_set = int(args[1])

# 第三引数をカレーセットの一日注文数orders_curry_setに代入
orders_curry_set = int(args[2])

# 価格表を辞書型で定義

price_dic ={
    'price_friedchicken_set':760,
    'price_curry_set':850,
}

# 売上salesに唐揚げ定食とカレーセットの一日の売り上げを代入

sales = (orders_friedchicken_set*price_dic['price_friedchicken_set']) + (orders_curry_set*price_dic['price_curry_set'])

print(sales, end ="")

