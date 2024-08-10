import pandas as pd
from math import *

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


def findSubstation(inputlatLong, substationLatLong):

    closestlatLong = [substationLatLong['SUB_LAT'][0], substationLatLong['SUB_LONG'][0]]
    row = 0
    closestDist = 0
    for i in range(len(substationLatLong)):
        testLat = substationLatLong['SUB_LAT'][i]
        testLong = substationLatLong['SUB_LONG'][i]
        closestDist = haversine(inputlatLong[0], inputlatLong[1], closestlatLong[0], closestlatLong[1])
        testDist = haversine(inputlatLong[0], inputlatLong[1], testLat, testLong)

        if testDist < closestDist:
            closestlatLong = [testLat, testLong]
            row  = i

    return closestDist, substationLatLong['SUB_ZIPCODE'][row]


realPoleData = pd.read_csv("/Users/arahan/Downloads/powerPoleDatav2.csv")
substationData = pd.read_csv("/Users/arahan/Downloads/Substationv4LatLong.csv")
realLat = realPoleData['POLE_LAT']
realLong = realPoleData['POLE_LONG']

lat = 0
long = 0
distance = 0
zipcode = 0

latitudes = []
longitudes = []
dist = []
zipcodes = []

for i in range(len(realLat)):
    latitude = realLat[i]
    longitude = realLong[i]
    #find nearest substation and get distance
    latitudes.append(latitude)
    longitudes.append(longitude)
    distance, zipcode = findSubstation([latitude, longitude], substationData)
    dist.append(distance)
    zipcodes.append(zipcode)


df = {'POLE_LAT': latitudes,
      'POLE_LONG': longitudes,
      'POLE_ZIPCODE': realPoleData['POLE_ZIPCODE'],
      'POLE_SUB_DIST': dist}

df = pd.DataFrame(df)
df.to_csv("/Users/arahan/Downloads/RealPoleLatLongZipcodeSubDist.csv")