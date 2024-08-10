import socket
import sys
from time import sleep
from struct import pack
import random
#set up signal transfer
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host, port = '192.168.68.122', 65000
server_address = (host, port)
#List consists of : LAT, LONG, TILT
poleData = [
    ['37.30156605', '-122.0148933', '0.0'],
    ['37.28886784', '-121.9980791', '0.0'],
    ['37.29991058', '-122.0096606', '0.0'],
    ['37.27779450', '-122.0209940', '0.0'],
    ['37.27615540', '-122.0146761', '0.0'],
    ['37.27967960', '-122.0145437', '0.0'],
    ['37.28646281', '-122.0034830', '0.0'],
    ['37.29700860', '-122.0127102', '0.0'],
    ['37.27955790', '-122.0213720', '0.0'],
    ['37.28298500', '-121.9914167', '0.0'],
]
pole = 0
tilt = ""
tiltAngle = 0
crit = 0

#trials
for i in range(20):
    for j in range(10):
        tiltNum = random.randint(0, 3)
        if tiltNum == 1:
            tiltAngle = '0.3'
        if tiltNum == 2:
            tiltAngle = '0.7'
        if tiltNum == 3:
            tiltAngle = '1.0'

        poleData[j][2] = tiltAngle
#sending signals

for i in range(len(poleData)):
        message = pack('11s 12s 3s', poleData[i][0].encode('utf-8'), poleData[i][1].encode('utf-8'), poleData[i][2].encode('utf-8'))
        sock.sendto(message, server_address)
        print("sent " + str(i) + " pole")
        sleep(10)

print(poleData)