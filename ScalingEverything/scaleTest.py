import numpy as np
from sklearn.preprocessing import MinMaxScaler
myArray = np.array([1, 5, 4, 9, 3, 2, 8, 7, 6, 10])
myArray = myArray.reshape(-1, 1)
scaler = MinMaxScaler()

myNewArray = scaler.fit_transform(myArray)
myNewArray = list(myNewArray)
myArray = list(myArray)
myNewArray.sort()
myArray.sort()
print(myNewArray)
print(myArray)