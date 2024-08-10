import pandas as pd

masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev7.csv")

myCol = masterDf['POLE_LAT']
myCol = list(myCol)

row = myCol.index(37.39908159)
print(row)
print(myCol[row])
print(masterDf['POLE_POP_SCALED'][row], masterDf['POLE_SUB_DIST_SCALED'][row], masterDf['POLE_ZONE'][row], masterDf['SYNTH_SENSOR_DATA'][row])