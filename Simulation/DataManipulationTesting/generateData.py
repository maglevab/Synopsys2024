import random
import pandas as pd
import numpy as np
import mysql.connector
from math import *


mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database='PowerPole'
)

mycursor = mydb.cursor()
query = "SELECT * FROM powerPoleLatLong;"
mycursor.execute(query)


results = []
for row in mycursor.fetchall():
    results.append(row)

#find average distance between all poles
avgLat = 0
avgLong = 0
count = 0
for i in range(len(results)):
    pole1 = results[i]
    for j in range(len(results)):
        if results[i] == results[j]:
            continue
        pole2 = results[j]
        #calc distance
        distLat = abs(pole1[0] - pole2[0])
        avgLat += distLat
        distLong = abs(pole1[1] - pole2[1])
        avgLong += distLong
        count += 1

avgLat /= count
avgLong /= count
avgLat = float(avgLat)
avgLong = float(avgLong)
print(type(avgLat))
print(avgLong)

startingPoleLat = 37.2795579000
startingPoleLong = -122.0213720000
newPolesLat = []
newPolesLong = []
randomNum = 0
for i in range(78):
    for j in range(78):
        randomNum = random.uniform(0, 2)
        startingPoleLong += randomNum * avgLong
        newPolesLat.append(startingPoleLat)
        newPolesLong.append(startingPoleLong)
        print(randomNum)
    randomNum = random.uniform(0, 2)
    print('-----')
    print(randomNum)
    print('-----')
    startingPoleLat += randomNum * avgLat
    startingPoleLong = -122.0213720000

data = {
    'POLE_LAT': newPolesLat,
    'POLE_LONG': newPolesLong
}

poleDf = pd.DataFrame(data)
poleDf.to_csv("/Users/arahan/Downloads/fakePoleDataPART2WITH6000.csv", index = False)
print("FILE EXPORTED")
