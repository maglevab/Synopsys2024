import mysql.connector
from math import *
import geopy


mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database='PowerPole'
)

mycursor = mydb.cursor()

mycursor = mydb.cursor()
query = 'SELECT * FROM powerPoleLatLong;'
mycursor.execute(query)

results = []
for row in mycursor.fetchall():
    results.append(row)


def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3959
    return c * r


subLat = 37.28105051
subLong = -122.0153074
query = ""
for i in range(len(results)):
    #calc distance
    dist = haversine(subLat, subLong, results[i][0], results[i][1])
    print(dist)
    #query = "UPDATE powerPoleLatLong SET POLE_SUB_DIST = {} WHERE POLE_LAT = {} AND POLE_LONG = {};".format(str(dist), results[i][0], results[i][1])
    #print(query)
    #print(results[i])
    #mycursor.execute(query)
mydb.commit()