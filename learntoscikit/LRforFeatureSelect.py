__author__ = 'arachis'
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel


iris = load_iris()
X, y = iris.data, iris.target
X.shape
lr = LogisticRegression(C=0.01, penalty="l1", dual=False).fit(X, y)
model = SelectFromModel(lr, prefit=True)
X_new = model.transform(X)
X_new.shape

