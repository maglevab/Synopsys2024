import pandas as pd
import warnings
import mysql.connector
import joblib
import socket
from struct import unpack
import numpy as np
import criticalityAlgorithmTable
from decimal import Decimal



# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '192.168.68.120', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)



mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database='powerPoleFINAL'
)

mycursor = mydb.cursor()

while True:
    # Wait for message
    message, address = sock.recvfrom(4096)

    lat, long, expectedCrit, sensorData = unpack('11s 12s 1s 3s', message)
    lat = float(lat)
    long = float(long)
    sensorData = float(sensorData)
    expectedCrit = int(expectedCrit)

    criticality = criticalityAlgorithmTable.calculateCriticality(Decimal(str(long)), sensorData)

    print("Criticality is: " + str(criticality) + ". The expected value is: " + str(expectedCrit))
    #stuff for updating server
    '''
    if sensorData != 2.0:
        #update SQL server
        critQuery = "UPDATE powerpoledatabasefinalv2 SET POLE_CRIT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(criticality), str(lat), str(long))
        sensorQuery = "UPDATE powerpoledatabasefinalv2 SET POLE_TILT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(sensorData), str(lat), str(long))
    else:

        critQuery = "UPDATE powerpoledatabasefinalv2 SET POLE_CRIT = '4' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(lat), str(long))
        sensorQuery = "UPDATE powerpoledatabasefinalv2 SET POLE_TILT = '{}' WHERE POLE_LAT = '{}' AND POLE_LONG = '{}';".format(str(sensorData), str(lat), str(long))

    print("updated database")
    mycursor.execute(critQuery)
    mycursor.execute(sensorQuery)
    mydb.commit()
    '''
