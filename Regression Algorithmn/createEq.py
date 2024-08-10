import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn.metrics import mean_squared_error, r2_score
# Load the data
df = pd.read_csv('/Users/arahan/Downloads/masterPowerPoleDatav7.csv')
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = ShuffleSplit(df[['POLE_POP_SCALED', 'POLE_SUB_DIST', 'POLE_ZONE', 'SYNTH_SENSOR_DATA']], df['POLE_CRIT_LABEL'], test_size=0.25)

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print(model.coef_)
print(model.intercept_)
print("C = {} X + {} Y + {} Z + {} A + {}".format(model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3], model.intercept_))
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))