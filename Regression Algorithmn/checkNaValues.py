import pandas as pd

df = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDatav7.csv")
print(df['POLE_CRIT_LABEL'].isnull())
