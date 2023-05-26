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

# 原価表を辞書型で定義

cost_dic = {
    'cost_friedchicken_set':0.323,
    'cost_curry_set':0.284,
}

# 唐揚げ定食の一日売上高をsales_friedchickenに代入
sales_friedchicken = orders_friedchicken_set*price_dic['price_friedchicken_set']

# カレーセットの一日売上高をsales_curry_setに代入
sales_curry_set = orders_curry_set*price_dic['price_curry_set']

# 唐揚げ定食の原価をcost_friedchickenに代入
cost_friedchicken = round(sales_friedchicken*cost_dic['cost_friedchicken_set'])

# カレーセットの原価をcost_curryに代入
cost_curry = round(sales_curry_set*cost_dic['cost_curry_set'])

# 唐揚げ定食の粗利をprofit_friedchicken_setに代入
profit_friedchicken_set = sales_friedchicken - cost_friedchicken

# カレーセットの粗利をprofit_curry_setに代入
profit_curry_set = sales_curry_set - cost_curry

sales = sales_friedchicken + sales_curry_set
cost = cost_friedchicken + cost_curry
profit = profit_friedchicken_set + profit_curry_set

print("売上高："+str(sales)+"、原価："+str(cost)+"、粗利："+str(profit),end="")