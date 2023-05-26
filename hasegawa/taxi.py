# 引数のモジュールをimport
import sys
args = sys.argv

# mathモジュールをimport
import math

# 第二引数を乗車距離taraveled_distanceに代入
traveled_distance = int(args[1])

# 初乗り運賃630円、距離料金98円、加算距離334mをそれぞれinitial_fare, distance_fare,distance_fare_rateに代入
initial_fare = 630
distance_fare = 98
distance_fare_rate = 344


# タクシー運賃をtaxi_fareに代入
taxi_fare = 0

# 乗車距離が1500mまでの場合、taxi_fareにinitial_fareに代入
if 1 <= traveled_distance <= 1500:
    taxi_fare = initial_fare
# タクシー運賃に、乗車距離が1500mを超える場合、初乗り運賃に344ｍ走るごとに98円を加算していく
else:
    taxi_fare = initial_fare + distance_fare*math.floor((traveled_distance-1500)//(distance_fare_rate)+1)

print(taxi_fare, end="")

