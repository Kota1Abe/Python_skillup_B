import sys
args = sys.argv

num_karaage=int(args[1])
num_curry=int(args[2])

karaage=760
curry=850
karaage_cost_rate=0.323
curry_cost_rate=0.284

karaage_sales=karaage*num_karaage
curry_sales=curry*num_curry
sales=karaage_sales+curry_sales

karaage_prime_cost=round(karaage_sales*karaage_cost_rate)
curry_prime_cost=round(curry_sales*curry_cost_rate)
prime_cost=karaage_prime_cost+curry_prime_cost

gross_profit=sales-prime_cost

print(f"売上高：{sales}、原価：{prime_cost}、粗利：{gross_profit}",end="")
