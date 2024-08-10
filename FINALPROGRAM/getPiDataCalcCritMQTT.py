import mysql.connector
import socket
import pandas as pd
from struct import unpack
import joblib
from decimal import Decimal
from Simulation.criticalityAlgorithmv2 import criticalityAlgorithmTable


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
host, port = '192.168.68.120', 65000
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
        criticality = criticalityAlgorithmTable.calculateCriticality(Decimal(str(long)), sensorData)
        print(criticality)
        #update SQL server
        critQuery = "UPDATE `powerpoledatabasefinalv2` SET `POLE_CRIT` = '{}' WHERE POLE_LONG = '{}';".format(str(criticality), str(long))
        sensorQuery = "UPDATE powerpoledatabasefinalv2 SET POLE_TILT = '{}' WHERE POLE_LONG = '{}'".format(str(sensorData), str(long))
    else:
        critQuery = "UPDATE powerpoledatabasefinalv2 SET POLE_CRIT = '4' WHERE POLE_LONG = '{}';".format(str(long))
        sensorQuery = "UPDATE powerpoledatabasefinalv2 SET POLE_TILT = '{}' WHERE POLE_LONG = '{}'".format(str(sensorData), str(long))

    mycursor.execute(critQuery)
    mycursor.execute(sensorQuery)

    mydb.commit()
