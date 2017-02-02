#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV


if __name__ == "__main__":
    # pandas读入
    data = pd.read_csv('10.Advertising.csv')    # TV、Radio、Newspaper、Sales
    x = data[['TV', 'Radio', 'Newspaper']]
    # x = data[['TV', 'Radio']]
    y = data['Sales']
    # print x
    # print y

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2017)
    # model = Lasso()
    model = Ridge()
    alpha_can = np.logspace(-3, 2, 10)
    lasso_model = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)
    lasso_model.fit(x_train, y_train)
    print '超参数：', lasso_model.best_params_

    y_hat = lasso_model.predict(np.array(x_test))
    print '参数最佳评分：',lasso_model.score(x_test, y_test)
    mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error
    print mse, rmse

    # t = np.arange(len(x_test))
    # mpl.rcParams['font.sans-serif'] = [u'simHei']
    # mpl.rcParams['axes.unicode_minus'] = False
    # plt.plot(t, y_test, 'r-', linewidth=2, label=u'真实数据')
    # plt.plot(t, y_hat, 'g-', linewidth=2, label=u'预测数据')
    # plt.title(u'线性回归预测销量', fontsize=18)
    # plt.legend(loc='upper right')
    # plt.grid()
    # plt.show()
