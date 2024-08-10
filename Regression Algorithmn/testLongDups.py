import pandas as pd

masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev7.csv")

masterlist = list(masterDf['POLE_CRIT_LABEL'])

print(masterlist.count(1))
print(masterlist.count(2))
print(masterlist.count(3))

#percentages
#1 - 18%
#2 - 48%
#3 - 34%