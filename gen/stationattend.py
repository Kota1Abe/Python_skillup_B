# モジュールをimport
import sys
args = sys.argv

#引数を変数に代入
num = int(args[1])
station_name = str(args[2])
distance = float(args[3])


from database import session
from stationtable import Stations


stations = Stations(
    seq = num,
    name = station_name,
    kilo = distance
    )

# Insert処理
session.add(stations)

# コミット
session.commit()