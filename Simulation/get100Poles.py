import pandas as pd
from random import randint
masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev7.csv")
poleData = []
previousNumbers = []

for i in range(300):
    num = randint(0, len(masterDf)-1)
    while num in previousNumbers:
        num = randint(0, len(masterDf))

    previousNumbers.append(num)
    temp = [str(masterDf['POLE_LAT'][num]), str(masterDf['POLE_LONG'][num]), '0.0']
    poleData.append(temp)


print(poleData)