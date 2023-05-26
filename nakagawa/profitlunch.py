import sys
args = sys.argv

#粗利：売上高に原価率をかけて算出した原価を売り上げから引いたもの

KARAAGE_VALUE = 760
KARAAGE_COST_RATE = 0.323
CURRY_VALUE = 850
CURRY_COST_RATE = 0.284

karaage_num = int(args[1])
curry_num = int(args[2])

karaage_sum = KARAAGE_VALUE * karaage_num
curry_sum = CURRY_VALUE * curry_num
sum = karaage_sum + curry_sum

karaage_cost = int(format(karaage_sum * KARAAGE_COST_RATE, '.0f'))
curry_cost = int(format(curry_sum * CURRY_COST_RATE, '.0f'))
cost = karaage_cost + curry_cost

karaage_profit = karaage_sum - karaage_cost
curry_profit = curry_sum - curry_cost
profit = karaage_profit + curry_profit

print(f'売上高：{sum}、原価：{cost}、粗利：{profit}', end="")
