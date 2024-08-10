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

for i in range(len(results)):
    query = "UPDATE powerpoledatabasefinalv2 SET POLE_CRIT = 0.0 WHERE POLE_LAT = {}".format(results[i][0])
    mycursor.execute(query)

mydb.commit()