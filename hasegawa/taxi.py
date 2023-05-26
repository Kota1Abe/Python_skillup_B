# 引数のライブラリをimport
import sys
args = sys.argv

traveled_distance = int(args[1])

intial_fare = 630
distance_fare = 98
distance_fare_rate = 344


# 初乗りタクシー運賃をtaxi_fareに代入
taxi_fare = 0

if 1 <= traveled_distance <= 1500:
    taxi_fare = intial_fare
else:
    taxi_fare = intial_fare + 

print(taxi_fare)

