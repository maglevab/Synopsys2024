import mysql.connector
import socket
import sys
from struct import unpack


def calccritindex(mycursor, lat, long, sensorData):
    roadWeight = 0.25
    zoneWeight = 0.1
    sensorWeight = 0.5
    distSubWeight = 0.5

    pole = []

    if(sensorData != 4):
        query = "SELECT * FROM powerPoleLatLong"
        mycursor.execute(query)
        results = []
        for row in mycursor.fetchall():
            results.append(row)

        for i in range(len(row)):
            if row[i][0] == lat and row[i][1] == long:
                pole = row[i]
                break

        poleProxRoadData = pole[8]
        poleZoneData = pole[9]
        poleDistSubData = pole[6]

        critIndex = (roadWeight * poleProxRoadData) + (zoneWeight * poleZoneData) + (sensorWeight * sensorData) + (distSubWeight * poleDistSubData)
        print("calculated critIndex")
        print(critIndex)
        return critIndex

    return 1


mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database='PowerPole'
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
    lat, long, sensorData = unpack('13s 15s f', message)
    lat = lat.decode('utf-8')
    long = long.decode('utf-8')
    print('X: {lat}, Y: {long}, Z: {sensorData}')
    critIndex = calccritindex(mycursor, lat, long, sensorData)
    mydb.commit()
    break