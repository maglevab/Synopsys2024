import pandas as pd

masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev7.csv")
labelingMatric = pd.read_csv('/Users/arahan/Downloads/criticalityLabelingMatrix.csv')

#Class Population
popClass = []
popData = masterDf['POLE_POP_SCALED']

for i in range(len(popData)):
    if popData[i] <= 1/3:
        popClass.append('Low')
    elif popData[i] <= 2/3:
        popClass.append("Medium")
    else:
        popClass.append("High")

masterDf['POP_CLASS'] = popClass

#Class Distance
distClass = []
distData = masterDf['POLE_SUB_DIST_SCALED']

for i in range(len(distData)):
    if 2/3 < distData[i] <= 1:
        distClass.append("High")
    elif distData[i] > 1/3:
        distClass.append("Medium")
    else:
        distClass.append('Low')

masterDf['DIST_CLASS'] = distClass

#Class Zone
zoneClass = []
zoneData = masterDf['POLE_ZONE']

for i in range(len(zoneData)):
    if zoneData[i] == 0:
        zoneClass.append("Urban")
    else:
        zoneClass.append("Forest")

masterDf['ZONE_CLASS'] = zoneClass

#Class Tilt Angle
tiltClass = []
tiltData = masterDf['POLE_TILT']

for i in range(len(tiltData)):
    if tiltData[i] == 1:
        tiltClass.append("High")
    elif tiltData[i] == 0.7:
        tiltClass.append("Medium")
    else:
        tiltClass.append("Low")

masterDf['TILT_CLASS'] = tiltClass

masterDf.to_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev8.csv")