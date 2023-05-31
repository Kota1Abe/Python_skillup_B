# 引数モジュールをimport

import sys
args = sys.argv

# データベース接続
from database import session

# テーブル定義
from distancedb_make import Stations

# 第二引数を出発駅の変数departure_stationに代入

departure_station = args[1] 

# 第三引数を到着駅の変数arrival_stationに代入

arrival_station = args[2]

distance_departure = session.query(Stations.kilo).filter_by(name = departure_station).first().kilo

distance_arrival = session.query(Stations.kilo).filter_by(name = arrival_station).first().kilo


distance_between_2points = abs(distance_departure) - (distance_arrival)

print(distance_arrival, end="")