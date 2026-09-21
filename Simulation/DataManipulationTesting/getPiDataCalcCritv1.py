import socket
import mysql
from struct import unpack

#initialize socket for data transfer
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host, port = '192.168.68.109', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)

#initialize sql database to update the database
mydb = mysql.connector.connect(
    host = 'localhost',
    port = '8889',
    user = 'root',
    password = 'root',
    database = 'PowerPole'
)
mycursor = mydb.cursor()

#loop for data transfer
while True:

    message, address = sock.recvfro(409)
