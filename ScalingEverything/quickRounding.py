import pandas as pd

df = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev4.csv")
sensorData = df['SYNTH_SENSOR_DATA']
for i in range(len(sensorData)):
    if sensorData[i] == 0.333333333:
        sensorData[i] = 0.3
    elif sensorData[i] == 0.666666667:
        sensorData[i] = 0.7
df.to_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev5.csv")