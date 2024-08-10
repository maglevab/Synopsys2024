from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
zipcodeData = pd.read_csv("/Users/arahan/Downloads/zipcodeDatav5.csv")
zipcodeData['zipcode'] = zipcodeData['zipcode'].apply(lambda x: '00' + str(x) if len(str(x)) == 3 else '0' + str(x) if len(str(x)) == 4 else str(x))

print(zipcodeData)

scaler = MinMaxScaler()
column_toBe_scaled = np.array(zipcodeData["population"])
column_toBe_scaled = column_toBe_scaled.reshape(-1, 1)
scaledColumn = scaler.fit_transform(column_toBe_scaled)
zipcodeData["population"] = scaledColumn
print(zipcodeData)
print(max(zipcodeData["population"]))
print(min(zipcodeData["population"]))
zipcodeData.to_csv('/Users/arahan/Downloads/scaledZipcodeData.csv', index = False)