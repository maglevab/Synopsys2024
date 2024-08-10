import pandas as pd

masterDf = pd.read_csv('/Users/arahan/Downloads/masterPowerPoleDatav5.csv')
print(masterDf['POLE_POP_SCALED'].unique())