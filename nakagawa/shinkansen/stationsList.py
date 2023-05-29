from database import session
from tables import Stations
import csv
from datetime import date

#holiday.csvを読み込む
filename = '/home/matcha-23training/Python_skillup_B/nakagawa/shinkansen/data/stations.csv'
with open(filename, encoding='utf-8_sig', newline='') as f:
    csvreader = csv.reader(f)
    seq = 0
    for row in csvreader:
        seq +=1
        stations = Stations(
            seq = seq,
            name = row[0],
            kilo = row[1],
        )
        session.add(stations)
        session.commit()