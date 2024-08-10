import pandas as pd
from math import *
import geopy

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

    for i in range(len(substationLatLong)):
        testLat = substationLatLong['SUB_LAT'][i]
        testLong = substationLatLong['SUB_LONG'][i]
        closestDist = haversine(inputlatLong[0], inputlatLong[1], closestlatLong[0], closestlatLong[1])
        testDist = haversine(inputlatLong[0], inputlatLong[1], testLat, testLong)

        if testDist < closestDist:
            closestlatLong = [testLat, testLong]

    return closestDist, closestlatLong


subdf = pd.read_csv("/Users/arahan/Downloads/Substationv4LatLong.csv")

inputLat = 37.30851986016577
inputLong = -121.9511797
subDist, sublatlong = findSubstation([inputLat, inputLong], subdf)
print(inputLat, inputLong, subDist, sublatlong)