import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
masterDf = pd.read_csv("/Users/arahan/Downloads/SynthAndRealLatLongZipcodeSubDist.csv")
data = np.array([0] * len(masterDf['POLE_SUB_DIST_SCALED']))
data = data.reshape(-1, 1)
print(data)
scaler = MinMaxScaler()
newData = scaler.fit_transform(data)
print(newData)
masterDf['POLE_SUB_DIST_SCALED'] = newData
print(masterDf['POLE_SUB_DIST_SCALED'])