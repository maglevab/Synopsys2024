import pandas as pd

masterDf = pd.read_csv('/Users/arahan/Downloads/masterPowerPoleDataLargev8.csv')
labelingDf = pd.read_csv("/Users/arahan/Downloads/criticalityLabelingMatrix.csv")

newMasterDf = pd.merge(masterDf, labelingDf, on=['Population', 'Distance', 'Zone', 'Tilt Angle'])
newMasterDf.to_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev9.csv")
