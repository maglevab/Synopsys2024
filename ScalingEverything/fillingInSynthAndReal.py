import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLarge.csv")
zipcodeDf = pd.read_csv("/Users/arahan/Downloads/scaledZipcodeData.csv")
masterSubDist = masterDf['POLE_SUB_DIST']
print(masterSubDist[:10])
#fill in zipcode column
masterDf = masterDf.merge(zipcodeDf, left_on='POLE_ZIPCODE', right_on='zipcode')
print(masterDf.head())
#scaling pole substation distance
print(type(masterSubDist[1]))
masterSubDist = np.array(masterSubDist)
masterSubDist = masterSubDist.reshape(-1, 1)

scaler = MinMaxScaler()
masterSubDistScaled = scaler.fit_transform(masterSubDist)
print(masterSubDistScaled)
masterDf['POLE_SUB_DIST_SCALED'] = masterSubDistScaled
#fill in pole_zone
zipcodeLabeling = {
    'zipcodes': [95008, 95070, 95032, 95051, 95014, 95118, 95125, 95111, 95123, 95138, 95013, 95148, 95110, 95112, 95050, 95122, 95133, 95116, 94085, 94086, 95131, 95054, 95035,95134],
    'class': [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
}
zipcodeLabeling = pd.DataFrame(zipcodeLabeling)
print(zipcodeLabeling.head())
masterDf = masterDf.merge(zipcodeLabeling, left_on='POLE_ZIPCODE', right_on='zipcodes')
print(masterDf['POLE_SUB_DIST_SCALED'])
masterDf.to_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev2.csv")