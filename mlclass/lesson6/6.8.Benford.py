# -*- coding:utf-8 -*-
# /usr/bin/python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from time import time
from scipy.special import factorial
import math

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = 'SimHei'


def top1(number, a):
    number /= a
    while number >= 10:
        number /= 10
        a *= 10
    return number, a


def top2(number, N2):
    while number >= N2:
        number /= 10
    n = number
    while number >= 10:
        number /= 10
    return n, number


def top3(number):
    number -= int(number)
    return int(10 ** number)


def top4(number):
    number -= int(number)
    frequency[int(10 ** number) - 1] += 1


if __name__ == '__main__':
    N = 100000
    x = range(1, N+1)
    frequency = np.zeros(9, dtype=np.int)
    f = 1
    print '开始计算...'
    t0 = time()
    # top1
    # a = 1
    # for t in x:
    #     f *= t
    #     i, a = top1(f, a)
    #     # print t, i, f, a
    #     frequency[i-1] += 1

    # top2
    # N2 = N ** 3
    # for t in x:
    #     f *= t
    #     f, i = top2(f, N2)
    #     frequency[i-1] += 1

    # Top 3：实现1
    # f = 0
    # for t in x:
    #     f += math.log10(t)
    #     frequency[top3(f) - 1] += 1

    # Top 3：实现2
    # y = np.cumsum(np.log10(x))
    # for t in y:
    #     frequency[top3(t) - 1] += 1

    # Top 4：本质与Top3相同
    y = np.cumsum(np.log10(x))
    map(top4, y)

    t1 = time()
    print '耗时：', t1 - t0
    print frequency
    t = np.arange(1, 10)
    plt.plot(t, frequency, 'r-', t, frequency, 'go', lw=2, markersize=8)
    for x,y in enumerate(frequency):
        plt.text(x+1.1, y, frequency[x], verticalalignment='top', fontsize=15)
    plt.title(u'%d!首位数字出现频率' % N, fontsize=18)
    plt.xlim(0.5, 9.5)
    plt.ylim(0, max(frequency)*1.03)
    plt.grid(b=True)
    plt.show()

    # 使用numpy
    # N = 170
    # x = np.arange(1, N+1)
    # f = np.zeros(9, dtype=np.int)
    # t1 = time()
    # y = factorial(x, exact=False)
    # z = map(top, y)
    # t2 = time()
    # print '耗时 = \t', t2 - t1
    # for t in z:
    #     f[t-1] += 1
    # print f
