from random import randint
import pandas as pd

masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev2.csv")
for i in range(len(masterDf['SYNTH_SENSOR_DATA'])):
    num = randint(1, 3)
    masterDf['SYNTH_SENSOR_DATA'][i] = num / 3

masterDf.to_csv('/Users/arahan/Downloads/masterPowerPoleDataLargev3.csv')