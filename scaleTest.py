from sklearn.preprocessing import MinMaxScaler
import numpy as np
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
data = data.reshape(-1, 1)
print(data)
scaler = MinMaxScaler()
newData = scaler.fit_transform(data)
print(newData)