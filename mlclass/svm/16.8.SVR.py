#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt


if __name__ == "__main__":
    N = 50
    np.random.seed(0)
    x = np.sort(np.random.uniform(0, 6, N), axis=0)
    y = 2*np.sin(x) + 0.1*np.random.randn(N)
    x = x.reshape(-1, 1)
    print 'x =\n', x
    print 'y =\n', y

    print 'SVR - RBF'
    svr_rbf = svm.SVR(kernel='rbf', gamma=0.2, C=100)
    svr_rbf.fit(x, y)
    print 'SVR - Linear'
    svr_linear = svm.SVR(kernel='linear', C=100)
    svr_linear.fit(x, y)
    print 'SVR - Polynomial'
    svr_poly = svm.SVR(kernel='poly', degree=3, C=100)
    svr_poly.fit(x, y)
    print 'Fit OK.'

    # 思考：系数1.1改成1.5
    x_test = np.linspace(x.min(), 1.1*x.max(), 100).reshape(-1, 1)
    y_rbf = svr_rbf.predict(x_test)
    y_linear = svr_linear.predict(x_test)
    y_poly = svr_poly.predict(x_test)

    plt.figure(figsize=(9, 8), facecolor='w')
    plt.plot(x_test, y_rbf, 'r-', linewidth=2, label='RBF Kernel')
    plt.plot(x_test, y_linear, 'g-', linewidth=2, label='Linear Kernel')
    plt.plot(x_test, y_poly, 'b-', linewidth=2, label='Polynomial Kernel')
    plt.plot(x, y, 'mo', markersize=6)
    plt.scatter(x[svr_rbf.support_], y[svr_rbf.support_], s=130, c='r', marker='*', label='RBF Support Vectors')
    plt.legend(loc='lower left')
    plt.title('SVR', fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.tight_layout(2)
    plt.show()
