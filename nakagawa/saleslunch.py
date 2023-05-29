import sys
args = sys.argv

#唐揚げ定食760円、カレーセット850円

KARAAGE_VALUE = 760
CURRY_VALUE = 850

karaage_num = int(args[1])
curry_num = int(args[2])

karaage_sum = KARAAGE_VALUE * karaage_num
curry_sum = CURRY_VALUE * curry_num

sum = karaage_sum + curry_sum
print(sum, end="")
