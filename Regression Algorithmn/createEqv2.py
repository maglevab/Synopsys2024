import pandas as pd
from sklearn.model_selection import ShuffleSplit
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDatav7.csv")
# Assuming you have your data loaded and features as X and target as y
X = df[['POLE_POP_SCALED', 'POLE_SUB_DIST', 'POLE_ZONE', 'SYNTH_SENSOR_DATA']]
y = df['POLE_CRIT_LABEL']
# Create an instance of ShuffleSplit for a single split
shuffle_split = ShuffleSplit(test_size=0.2)

# Get the train-test split indices for a single split
train_index, test_index = next(shuffle_split.split(X))

# Split the data into training and test sets
X_train, X_test = X.iloc[train_index], X.iloc[test_index]
y_train, y_test = y.iloc[train_index], y.iloc[test_index]

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print('The mean squared error is:', mean_squared_error(y_test, y_pred))
print('The R-squared score is:', r2_score(y_test, y_pred))
print(train_index, test_index)