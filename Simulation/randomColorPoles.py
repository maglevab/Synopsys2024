import mysql.connector
import pandas as pd
from random import randint
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

df = pd.DataFrame(results)
print(df[8])
for i in range(1000):
  if randint(0, 1) == 0:
    query = "UPDATE powerpoledatabasefinalv2 SET POLE_CRIT = {} WHERE POLE_LONG = {};".format(randint(0, 4), str(df[1][i]))
    print(query)
    mycursor.execute(query)

mydb.commit()