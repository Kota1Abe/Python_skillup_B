import sys
args = sys.argv
from database import session
from tables import Stations

#出発駅と到着駅を入力
departure_station = args[1]
arrival_station = args[2]

departure_distance = session.query(Stations.kilo).filter(Stations.name == departure_station).first()
arrival_distance = session.query(Stations.kilo).filter(Stations.name == arrival_station).first()

#駅間の距離を計算
distance = arrival_distance[0] - departure_distance[0]
print(distance)

