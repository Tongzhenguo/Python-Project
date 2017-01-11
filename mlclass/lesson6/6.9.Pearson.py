#!/usr/bin/python
#  -*- coding:utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = 'SimHei'


def calc_pearson(x, y):
    std1 = np.std(x)
    # np.sqrt(np.mean(x**2) - np.mean(x)**2)
    std2 = np.std(y)
    cov = np.cov(x, y, bias=True)[0,1]
    return cov / (std1 * std2)


def intro():
    N = 10
    x = np.random.rand(N)
    y = 2 * x + np.random.randn(N) * 0.1
    print x
    print y
    print '系统计算：', stats.pearsonr(x, y)[0]
    print '手动计算：', calc_pearson(x, y)


def rotate(x, y, theta=45):
    data = np.vstack((x, y))
    # print data
    mu = np.mean(data, axis=1)
    mu = mu.reshape((-1, 1))
    # print mu
    data -= mu
    # print data
    theta *= (np.pi / 180)
    c = np.cos(theta)
    s = np.sin(theta)
    m = np.array(((c, -s), (s, c)))
    return m.dot(data) + mu


def pearson(x, y, tip):
    clrs = list('rgbmycrgbmycrgbmycrgbmyc')
    plt.figure(figsize=(10, 8), facecolor='w')
    for i, theta in enumerate(np.linspace(0, 90, 6)):
        xr, yr = rotate(x, y, theta)
        p = stats.pearsonr(xr, yr)[0]
        # print calc_pearson(xr, yr)
        print '旋转角度：', theta, 'Pearson相关系数：', p
        str = u'相关系数：%.3f' % p
        plt.scatter(xr, yr, s=40, alpha=0.9, linewidths=0.5, c=clrs[i], marker='o', label=str)
    plt.legend(loc='upper left', shadow=True)
    plt.xlabel(u'X')
    plt.ylabel(u'Y')
    plt.title(u'Pearson相关系数与数据分布：%s' % tip, fontsize=18)
    plt.grid(b=True)
    plt.show()


if __name__ == '__main__':
    # warnings.filterwarnings(action='ignore', category=RuntimeWarning)
    np.random.seed(0)

    # intro()

    N = 1000
    # tip = u'一次函数关系'
    # x = np.random.rand(N)
    # y = np.zeros(N) + np.random.randn(N)*0.001

    # tip = u'二次函数关系'
    # x = np.random.rand(N)
    # y = x ** 2 #+ np.random.randn(N)*0.002

    # tip = u'正切关系'
    # x = np.random.rand(N) * 1.4
    # y = np.tan(x)

    # tip = u'二次函数关系'
    # x = np.linspace(-1, 1, 101)
    # y = x ** 2

    tip = u'椭圆'
    x, y = np.random.rand(2, N) * 60 - 30
    y /= 5
    idx = (x**2 / 900 + y**2 / 36 < 1)
    x = x[idx]
    y = y[idx]

    pearson(x, y, tip)
