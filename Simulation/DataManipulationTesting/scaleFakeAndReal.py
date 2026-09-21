import mysql.connector
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
realData = [
    0.0525334,
    0.072846,
    0.0938396,
    0.116963,
    0.137613,
    0.141921,
    0.126611,
    0.141786,
    0.134416,
    0.164614,
    0.186405,
    0.184545,
    0.204033,
    0.19666,
    0.197249,
    0.208857,
    0.16121,
    0.126065,
    0.129073,
    0.144258,
    0.14227,
    0.147738,
    0.13255,
    0.17667,
    0.204591,
    0.227121,
    0.261433,
    0.244805,
    0.296817,
    0.333199,
    0.410637,
    0.405779,
    0.433046,
    0.479559,
    0.516276,
    0.552052,
    0.551847,
    0.544532,
    0.528015,
    0.384797,
    0.424764,
    0.422602,
]

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database='PowerPole'
)

mycursor = mydb.cursor()
query = "SELECT * FROM powerPoleLatLong2;"
mycursor.execute(query)

results = []
for row in mycursor.fetchall():
    results.append(row)

totalPoleData = []
fakeDf = pd.read_csv("/Users/arahan/Downloads/fakeData4SQLv2.csv")
for i in range(len(fakeDf['POLE_SUB_DIST'])):
  totalPoleData.append(fakeDf['POLE_SUB_DIST'][i])

for i in range(len(realData)):
  totalPoleData.append(realData[i])
print(totalPoleData)
totalPoleData = np.array(totalPoleData)
data = totalPoleData.reshape(-1, 1)
scaler = MinMaxScaler()
newData = scaler.fit_transform(data)
newDf = pd.DataFrame(newData)
newDf.to_csv("/Users/arahan/Downloads/scaledSubstationDataWithFakeAndReal.csv", index=False)
print(newDf)
print(min(newDf))
print(max(newDf))