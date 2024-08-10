import pandas as pd
import socket
from struct import unpack

masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev7.csv")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '192.168.68.120', 65000
server_address = (host, port)

#coefficients
popC = 0.4
distC = 0.5
zoneC = 1
tiltC = 1.1
def getIndex(long):
    poleCol = list(masterDf['POLE_LONG'])
    return poleCol.index(long)

def calculateCriticality(long, sensorData):
    row = getIndex(long)
    return popC * masterDf['POLE_POP_SCALED'][row] + distC * masterDf['POLE_SUB_DIST_SCALED'][row] + zoneC * masterDf['POLE_ZONE'][row] + tiltC * sensorData


while True:
    message, address = sock.recvfrom(4096)

    lat, long, sensorData = unpack('11s 12s 3s', message)
    lat = float(lat)
    long = float(long)
    sensorData = float(sensorData)
    print("Criticality is " + str(calculateCriticality(long, sensorData)))




