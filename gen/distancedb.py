# 引数モジュールをimport
import sys
args = sys.argv
from database import session
from stationtable import Stations

#出発と到着を入力
departure = args[1]
arrival = args[2]

departure_distance = session.query(Stations.kilo).filter(Stations.name == departure).first()
arrival_distance = session.query(Stations.kilo).filter(Stations.name == arrival).first()

print(departure_distance)
print(arrival_distance)

#距離の計算
distance = arrival_distance[0] - departure_distance[0]

#距離がマイナスになった時
if distance < 0:
    distance = distance * (-1)
    print(round(distance,2))
else:
    print(distance)