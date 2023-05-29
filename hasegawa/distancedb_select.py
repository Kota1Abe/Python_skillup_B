# 引数モジュールをimport

import sys
args = sys.argv

# データベース接続
from database import session

# テーブル定義
from distancedb_make import Stations

session