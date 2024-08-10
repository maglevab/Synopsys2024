import pandas as pd
import mysql.connector

fakePoleData = pd.read_csv("/Users/arahan/Downloads/fakePoleDatav5.csv", encoding = 'utf8')

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database='PowerPole'
)

mycursor = mydb.cursor()

fakePoleLat = fakePoleData['POLE_LAT']
fakePoleLong = fakePoleData['POLE_LONG']
