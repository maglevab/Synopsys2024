import pandas as pd
from math import *


def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3959
    return c * r


def findSubstation(inputlatLong, substationLatLong):
    closestlatLong = [substationLatLong['SUB_LAT'][0], substationLatLong['SUB_LONG'][0]]
    closestDist = 0
    zipcode = 0

    for i in range(len(substationLatLong)):
        testLat = substationLatLong['SUB_LAT'][i]
        testLong = substationLatLong['SUB_LONG'][i]
        closestDist = haversine(inputlatLong[0], inputlatLong[1], closestlatLong[0], closestlatLong[1])
        testDist = haversine(inputlatLong[0], inputlatLong[1], testLat, testLong)

        if testDist < closestDist:
            closestlatLong = [testLat, testLong]
            zipcode = substationLatLong['SUB_ZIPCODE'][i]

    return closestDist, closestlatLong, zipcode


substationDf = pd.read_csv("/Users/arahan/Downloads/Substationv4LatLong.csv")
fakeData = pd.read_csv("/Users/arahan/Downloads/fakePoleDataPART2WITH6000.csv", encoding='utf8')
print(fakeData)

poleLat = fakeData['POLE_LAT']
poleLong = fakeData['POLE_LONG']
poleDist = []
poleZip = []

subLatLong = []
subDist = 0
# calculate the distance from the CLOSEST substation
for i in range(len(poleLat)):
    tempLat = poleLat[i]
    tempLong = poleLong[i]
    # find closest substation and distance to that substation
    subDist, subLatLong, zipcode = findSubstation([tempLat, tempLong], substationDf)
    print(subDist, subLatLong, zipcode, i)
    poleDist.append(subDist)
    poleZip.append(zipcode)

print(poleDist)
fakeData['POLE_SUB_DIST'] = poleDist
fakeData['POLE_ZIPCODE'] = poleZip
fakeData.to_csv("/Users/arahan/Downloads/synthPoleData6000SubDist.csv")


