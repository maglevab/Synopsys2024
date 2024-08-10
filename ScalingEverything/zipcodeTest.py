import pandas as pd

df = pd.read_csv('/Users/arahan/Downloads/masterPowerPoleDataLargev5.csv')

populations = df['POLE_POP_SCALED'].unique()
populations.sort()
length = len(populations)
print(populations)
print(len(populations))
print(populations[:length//3])
print(populations[length//3: 2*length//3])
print(populations[2*length//3:])
