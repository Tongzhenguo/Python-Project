### Gradient Boosting regression

### use Gradient Boosting on the borrower credit dataset.
## This example fits a Gradient Boosting model with Exponential loss and 100 regression trees of depth 5

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.utils import shuffle
#load data
train_x_csv = pd.read_csv("F:\code\Python-Project\dataset\\borrower_credit\\train_x.csv")
train_y_csv = pd.read_csv("F:\code\Python-Project\dataset\\borrower_credit\\train_y.csv")
test_csv = pd.read_csv("F:\code\Python-Project\dataset\\borrower_credit\\test_x.csv")
test_x = test_csv.drop(test_csv.columns[[0]],axis=1).values

#analysis data
# print train_y_csv[train_y_csv.y==0].count() #1542
# print train_y_csv[train_y_csv.y==1].count() #13458

# extend num(negtive) to the num(positive)
y_0 = train_y_csv[train_y_csv.y == 0]
merge = pd.merge(train_x_csv, y_0, how="inner", left_on=train_x_csv.uid,
                     right_on=y_0.uid)
X_ = train_x_csv.drop(train_x_csv.columns[[0]],axis=1) #index' axis = 0
for i in range(13458 / 1542 ):
    train_y_csv = train_y_csv.append(y_0)
    X_ = X_.append(merge.drop(merge.columns[[0,-2, -1]], axis=1))
X = X_.values
y = train_y_csv["y"].values

#random split train set
X, y = shuffle(X, y, random_state=13)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)
X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

#Fit regression model
params = {'n_estimators': 100, 'max_depth': 5, 'min_samples_split': 10,
          'learning_rate': 0.01, 'loss': 'ls',"warm_start":"True"}
clf = ensemble.GradientBoostingRegressor(**params)
clf.fit(X_train, y_train)
from sklearn.externals import joblib
joblib.dump(clf, "train_model.m")
mse = mean_squared_error(y_test, clf.predict(X_test))
print("MSE: %.4f" % mse)

# compute test set deviance
test_score = np.zeros((params['n_estimators'],), dtype=np.float64)
for i, y_pred in enumerate(clf.staged_predict(X_test)):
    test_score[i] = clf.loss_(y_test, y_pred)

# Plot training deviance
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, clf.train_score_, 'b-',
         label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
         label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')

# predict test set
predict = clf.predict(test_x)
uid_ = test_csv["uid"]
s = pd.Series(list(uid_.values),name="uid")
pd.DataFrame(predict,index=s,dtype="float64",columns=["score"])\
    .to_csv("F:\code\Python-Project\dataset\\borrower_credit\predict_gbdt.csv",encoding="utf-8")

#Plot feature importance
feature_importance = clf.feature_importances_
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
sorted_id = sorted_idx[1069:]
pos = np.arange(sorted_id.shape[0]) + .5
plt.subplot(1, 1, 1)
plt.barh(pos, feature_importance[sorted_id], align='center')
plt.yticks(pos, sorted_id)
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()

## store top 70 importance feature
pd.DataFrame(X[:,sorted_id],index=list(range(X.shape[0])),columns=sorted_id).\
    to_csv("F:\code\Python-Project\dataset\\borrower_credit\select_feature_train_x.csv")

pd.DataFrame(test_x[:,sorted_id],index=list(range(test_x.shape[0])),columns=sorted_id).\
    to_csv("F:\code\Python-Project\dataset\\borrower_credit\select_feature_test_x.csv")

