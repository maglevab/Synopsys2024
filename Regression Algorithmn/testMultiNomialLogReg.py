import pandas as pd
import joblib
from numpy import mean, std
from collections import Counter
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
from sklearn.metrics import f1_score
masterDf = pd.read_csv("/Users/arahan/Downloads/masterPowerPoleDataLargev9.csv")
X = masterDf[['POLE_POP_SCALED', 'POLE_SUB_DIST_SCALED', 'POLE_ZONE', 'POLE_TILT']]
y = masterDf['POLE_CRIT_LABEL']

print(X.shape, y.shape)
print(Counter(y))

model = LogisticRegression(multi_class='multinomial', solver='lbfgs')

cv = RepeatedStratifiedKFold(n_splits = 10, n_repeats = 3, random_state=1)


model.fit(X, y)

n_scores = cross_val_score(model, X, y, scoring='accuracy', cv = cv, n_jobs = 1)
print(n_scores)
scores = pd.Series(n_scores)
print(scores)
filename = '/Users/arahan/Downloads/synopsysModel2024Finalv4.sav'
joblib.dump(model, filename)


row = [0.397310299, 0.722581939, 0,	0.3]
yhat = model.predict_proba([row])
print('predicted probabilities: %s' %yhat[0])
print(list(yhat[0]).index(max(yhat[0]))+ 1)


