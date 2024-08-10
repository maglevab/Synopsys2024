import mysql.connector
import socket
import sys
from struct import unpack

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
host, port = '192.168.68.109', 65000
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
    print(f'X: {lat}, Y: {long}, Z: {sensorData}')
    query = "UPDATE powerPoleLatLong SET POLE_SENSOR_DATA = {} WHERE POLE_LAT = {} AND POLE_LONG = {};".format(str(sensorData), lat, long)
    print(query)
    mycursor.execute(query)
    print("EXECUTED QUERY")
    mydb.commit()
    break