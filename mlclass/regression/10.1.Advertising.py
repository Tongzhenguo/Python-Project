#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pprint import pprint


if __name__ == "__main__":
    path = '10.Advertising.csv'

    # pandas读入
    data = pd.read_csv(path)    # TV、Radio、Newspaper、Sales
    # x = data[['TV', 'Radio', 'Newspaper']]
    x = data[['TV', 'Radio']]
    y = data['Sales']

    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    #
    # 绘制1(不直观)
    # plt.plot(data['TV'], y, 'ro', label='TV')
    # plt.plot(data['Radio'], y, 'g^', label='Radio')
    # plt.plot(data['Newspaper'], y, 'mv', label='Newspaer')
    # plt.legend(loc='lower right')
    # plt.grid()
    # plt.show()
    #
    # # 绘制2（发现y和Newspaper线性不相关）
    # plt.figure(figsize=(9,12))
    # plt.subplot(311)
    # plt.plot(data['TV'], y, 'ro')
    # plt.title('TV')
    # plt.grid()
    # plt.subplot(312)
    # plt.plot(data['Radio'], y, 'g^')
    # plt.title('Radio')
    # plt.grid()
    # plt.subplot(313)
    # plt.plot(data['Newspaper'], y, 'b*')
    # plt.title('Newspaper')
    # plt.grid()
    # plt.tight_layout()
    # plt.show()

    #random_state是随机化种子，保证训练数据相同，模型可重现；默认参数是随机的，不保证重现
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=2017)
    # print x_train, y_train
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    # print model ##拟合出来的模型参数
    print linreg.coef_
    print linreg.intercept_
    #综上，sales = 0.04 * TV + 0.19 * RADIO + 3.16

    y_hat = linreg.predict(np.array(x_test))
    mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error
    print mse, rmse

    t = np.arange(len(x_test))
    plt.plot(t, y_test, 'r-', linewidth=2, label=u'真实数据')
    plt.plot(t, y_hat, 'g-', linewidth=2, label=u'预测数据')
    plt.legend(loc='upper right')
    plt.title(u'线性回归预测销量', fontsize=18)
    plt.grid()
    plt.show()
