# coding=utf-8
from sklearn import svm

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

if __name__ == "__main__":

    data = pd.read_csv('test.csv')
    print( data.head() )

    x = data[['d1','d2']].values
    y = data['label'].values

    #
    clf = svm.SVC( kernel='linear')
    clf.fit(x, y)
    y_hat = clf.predict(x)
    print(y_hat)


    clf = svm.SVC( kernel='rbf' )
    clf.fit(x, y)
    y_hat = clf.predict(x)
    print(y_hat)


    #多项式核a（x1+x2）^2 + c => poly => 0.5*(1- x1 * x2)
    x = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
    y = np.array([0, 1, 1, 0])
    clf = svm.SVC(kernel='poly', degree=2)
    clf.fit(x, y)
    y_hat = clf.predict(x)
    print(y_hat)

    #树模型没有线性不可分的问题，可以处理非线性数据
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    model = DecisionTreeClassifier(criterion='entropy', max_depth=2)
    model = model.fit(x,y)
    y_test_hat = model.predict(x)
    print(y_test_hat)
