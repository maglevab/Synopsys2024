import pandas as pd
import warnings
import mysql.connector
import joblib
import socket
from struct import unpack
import numpy as np
from sklearn.metrics import f1_score
masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev9.csv")
model = joblib.load('/Users/arahan/Downloads/synopsysModel2024Finalv3.sav')

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '192.168.68.120', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)

def getIndex(long):
    poleCol = list(masterDf['POLE_LONG'])
    return poleCol.index(long)


def calculateCriticality(long, sensorData):
    row = getIndex(long)
    data = [masterDf['POLE_POP_SCALED'][row], masterDf['POLE_SUB_DIST_SCALED'][row], masterDf['POLE_ZONE'][row],
            sensorData]
    crit = model.predict_proba([data])
    critList = list(crit[0])
    return critList.index(max(critList)) + 1
'''
mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database='PowerPole'
)

mycursor = mydb.cursor()
'''
acc = 0
cnt = 0
avgTrials = []
numTrials = 999
x_True = np.array([])
y_Pred = np.array([])

errorFreq = {'11': 0, '12': 0, '13': 0, '21': 0, '22': 0, '23': 0, '31': 0, '32': 0, '33': 0}
while True:
    # Wait for message
    message, address = sock.recvfrom(4096)

    lat, long, sensorData = unpack('11s 12s 3s', message)
    lat = float(lat)
    long = float(long)
    sensorData = float(sensorData)
    if sensorData == -10:
        #calculate averages
        avg = acc/300
        acc = 0
        avgTrials.append(avg)

        cnt += 1
        print(cnt)
        if cnt == numTrials:
            break
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        criticality = calculateCriticality(long, sensorData)

    #stuff for updating server
    '''
    #calculate criticality
    if sensorData != 2.0:
        #update SQL server
        critQuery = "UPDATE powerpoledatabasefinal SET POLE_CRIT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(criticality), str(lat), str(long))
        sensorQuery = "UPDATE powerpoledatabasefinal SET POLE_TILT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}'".format(str(sensorData), str(lat), str(long))
    else:

        critQuery = "UPDATE powerpoledatabasefinal SET POLE_CRIT = '4' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(lat), str(long))
        sensorQuery = "UPDATE powerpoledatabasefinal SET POLE_TILT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}'".format(str(sensorData), str(lat), str(long))

    print("updated database, checking accuracy")
    '''
    index = getIndex(long)
    actualCrit = masterDf['POLE_CRIT_LABEL'][index]

    errorFreq[str(actualCrit) + str(criticality)] += 1
    x_True = np.append(x_True, actualCrit)
    y_Pred = np.append(y_Pred, criticality)
    if actualCrit == criticality:


        acc += 1

    #mycursor.execute(critQuery)
    #mycursor.execute(sensorQuery)

    #mydb.commit()
num = 0
for i in avgTrials:
    num += i
    print("average is " + str(i * 100) + "%")
print("FINAL AVERAGE IS: " + str((num/len(avgTrials))*100) + "%")
print(errorFreq)
print(x_True)
print(y_Pred)
print(f1_score(x_True, y_Pred, average='macro'))
print(f1_score(x_True, y_Pred, average='micro'))
print(f1_score(x_True, y_Pred, average='weighted'))