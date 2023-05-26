# 引数モジュールをimport

import sys
args = sys.argv

num = int(args[1])
st_name = str(args[2])
dis = float(args[3])


from database import session

from distancedb_make import Stations
                  
