import joblib
model = joblib.load('/Users/arahan/Downloads/synopsysModel2024Final.sav')

row = [0.9, 0.0, 1,	1]
yhat = model.predict_proba([row])
print('predicted probabilities: %s' %yhat[0])
yhatList = list(yhat[0])
print(yhatList.index(max(yhatList)))