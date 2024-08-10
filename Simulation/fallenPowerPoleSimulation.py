import mysql.connector
import socket
import pandas as pd
from struct import unpack
import joblib
masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev7.csv")
model = joblib.load('/Users/arahan/Downloads/synopsysModel2024Finalv2.sav')

def getIndex(long):
    poleCol = list(masterDf['POLE_LONG'])
    return poleCol.index(long)

def calculateCriticality(long, sensorData):
    row = getIndex(long)
    data = [masterDf['POLE_POP_SCALED'][row], masterDf['POLE_SUB_DIST_SCALED'][row], masterDf['POLE_ZONE'][row],sensorData]
    crit = model.predict_proba([data])
    critList = list(crit[0])
    return critList.index(max(critList)) + 1

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database='powerPoleFINAL'
)

mycursor = mydb.cursor()

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '192.168.68.122', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)

while True:
    # Wait for message
    message, address = sock.recvfrom(4096)

    print(f'Received {len(message)} bytes:')
    lat, long, sensorData = unpack('11s 12s 3s', message)
    lat = float(lat)
    long = float(long)
    sensorData = float(sensorData)

    print('got here')
    print(lat, long, sensorData)
    #calculate criticality
    if sensorData != 2.0:
        criticality = calculateCriticality(long, sensorData)
        print(criticality)
        #update SQL server
        critQuery = "UPDATE powerpoledatabasefinal SET POLE_CRIT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(criticality), str(lat), str(long))
        sensorQuery = "UPDATE powerpoledatabasefinal SET POLE_TILT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}'".format(str(sensorData), str(lat), str(long))
    else:
        critQuery = "UPDATE powerpoledatabasefinal SET POLE_CRIT = '4' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(lat), str(long))
        sensorQuery = "UPDATE powerpoledatabasefinal SET POLE_TILT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}'".format(str(sensorData), str(lat), str(long))

    mycursor.execute(critQuery)
    mycursor.execute(sensorQuery)

    mydb.commit()

