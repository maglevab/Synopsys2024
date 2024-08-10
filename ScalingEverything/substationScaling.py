from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

data = np.array([
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
])
print(data)
data = data.reshape(-1, 1)
scaler = MinMaxScaler()
newData = scaler.fit_transform(data)
newDf = pd.DataFrame(newData)
#newDf.to_csv("/Users/arahan/Downloads/scaledSubstationData.csv", index=False)
print(newDf)