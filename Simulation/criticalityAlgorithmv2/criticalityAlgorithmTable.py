from decimal import Decimal

import pandas as pd

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database='powerPoleFINAL'
)

mycursor = mydb.cursor()
query = 'SELECT * FROM powerpoledatabasefinalv2;'
mycursor.execute(query)
results = []
for row in mycursor.fetchall():
    results.append(row)
#table headers:
# 0 -> PoleLat
# 1 -> PoleLong
# 2 -> PoleZipcode
# 3 -> PolePopulationScaled
# 4 -> PoleSubDist
# 5 -> PoleSubDistScaled
# 6 -> PoleZone
# 7 -> FakeOrSynth
# 8 -> PoleCritLabel
masterDf = pd.DataFrame(results)

query = "SELECT * FROM criticalityScoringRulesEngine"
mycursor.execute(query)
# 0 -> Population
# 1 -> Distance
# 2 -> Zone
# 3 -> TiltAngle
# 4 -> CriticalityLabel
criticalityRules = []
for row in mycursor.fetchall():
    criticalityRules.append(row)

criticalityRulesDf = pd.DataFrame(criticalityRules)

#'''
#Long must be Decimal(STRING)
def getIndex(long):
    poleCol = list(masterDf[1])
    return poleCol.index(long)

#rates population around power pole
def scalePopulationScore(pop):
    pop = float(pop)
    if pop < 1/3:
        return "Low"
    elif pop < 2/3:
        return "Medium"
    return "High"

#rates distance to substation from power pole
def scaleDistanceScore(dist):
    dist = float(dist)
    if dist < 1 / 3:
        return "Low"
    elif dist < 2 / 3:
        return "Medium"
    return "High"

#rates zone around power pole
def scaleZoneScore(zone):
    if zone == 0:
        return "Urban"
    return "Forest"

#rates tilt angle of power pole
def scaleTiltAngleScore(angle):
    if angle == 0.3:
        return "Low"
    elif angle == 0.7:
        return "Medium"
    return "High"

def calculateCriticality(long, sensorData):
    row = getIndex(long)
    population = scalePopulationScore(masterDf[3][row])
    substationDist = scaleDistanceScore(masterDf[5][row])
    zone = scaleZoneScore(masterDf[6][row])
    tiltAngle = scaleTiltAngleScore(sensorData)

    for i in range(len(criticalityRulesDf)):
        if criticalityRulesDf[0][i] == population and criticalityRulesDf[1][i] == substationDist and criticalityRulesDf[2][i] == zone and criticalityRulesDf[3][i] == tiltAngle:
            return criticalityRulesDf[4][i]


