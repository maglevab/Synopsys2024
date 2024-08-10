import pandas as pd

masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev3.csv")
zipcodeLabeling = {
    'zipcodes': [95008, 95070, 95032, 95051, 95014, 95118, 95125, 95111, 95123, 95138, 95013, 95148, 95110, 95112, 95050, 95122, 95133, 95116, 94085, 94086, 95131, 95054, 95035,95134],
    'class': [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
}
zipcodeLabeling = pd.DataFrame(zipcodeLabeling)
print(zipcodeLabeling.head())
masterDf = masterDf.merge(zipcodeLabeling, left_on='POLE_ZIPCODE', right_on='zipcodes')

zipcodeDf = pd.read_csv('/Users/arahan/Downloads/scaledZipcodeData.csv')
masterDf = masterDf.merge(zipcodeDf, left_on='POLE_ZIPCODE', right_on='zipcode')
masterDf.to_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev4.csv")