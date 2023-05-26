from datetime import date
from database import session
from maketable_station import Stations_make
import sys

args = sys.argv

city1=args[1]
city2=(args[2])

name1=session.query(Stations_make.kilo).filter_by(name=city1).all()
name2=session.query(Stations_make.kilo).filter_by(name=city2).all()

distance1=name1[0][0]
distance2=name2[0][0]

result=distance1-distance2

#距離がマイナスになった時
if result < 0:
    result = result*(-1)

print(round(result,2))

