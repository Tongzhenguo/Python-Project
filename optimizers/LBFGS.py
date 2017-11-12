# coding=utf-8
'''
    L-BFGS and
'''
from __future__ import print_function
from numpy import *
import matplotlib.pyplot as plt


def lbfgs(fun, gfun, x0):
    '''
    限制内存-拟牛顿迭代算法实现
    :param fun:原函数
    :param gfun:导函数
    :param x0:自变量
    :return:误差值
    '''
    result = []  # 保留最终的结果
    maxk = 500  # 最大的迭代次数
    rho = 0.55
    sigma = 0.4

    H0 = eye(shape(x0)[0])

    # s和y用于保存最近m个，这里m取6
    s = []
    y = []
    m = 6

    k = 1
    gk = mat(gfun(x0))  # 计算梯度
    dk = -H0 * gk
    while (k < maxk):
        n = 0
        mk = 0
        gk = mat(gfun(x0))  # 计算梯度
        while (n < 20):
            newf = fun(x0 + rho ** n * dk)
            oldf = fun(x0)
            if (newf < oldf + sigma * (rho ** n) * (gk.T * dk)[0, 0]):
                mk = n
                break
            n = n + 1

        # LBFGS校正
        x = x0 + rho ** mk * dk
        # print x

        # 保留m个
        if k > m:
            s.pop(0)
            y.pop(0)

        # 计算最新的
        sk = x - x0
        yk = gfun(x) - gk

        s.append(sk)
        y.append(yk)

        # two-loop的过程
        t = len(s)
        qk = gfun(x)
        a = []
        for i in range(t):
            alpha = (s[t - i - 1].T * qk) / (y[t - i - 1].T * s[t - i - 1])
            qk = qk - alpha[0, 0] * y[t - i - 1]
            a.append(alpha[0, 0])
        r = H0 * qk

        for i in range(t):
            beta = (y[i].T * r) / (y[i].T * s[i])
            r = r + s[i] * (a[t - i - 1] - beta[0, 0])

        if (yk.T * sk > 0):
            dk = -r

        k = k + 1
        x0 = x
        result.append(fun(x0))

    return result

if __name__ == '__main__':
    # fun，原函数
    fun = lambda x: 100 * (x[0, 0] ** 2 - x[1, 0]) ** 2 + (x[0, 0] - 1) ** 2

    # gfun，导函数
    def gfun(x):
        result = zeros((2, 1))
        result[0, 0] = 400 * x[0, 0] * (x[0, 0] ** 2 - x[1, 0]) + 2 * (x[0, 0] - 1)
        result[1, 0] = -200 * (x[0, 0] ** 2 - x[1, 0])
        return result

    x0 = mat([[-1.2], [1]])
    result = lbfgs(fun, gfun, x0)
    print(result)

    n = len(result)
    ax = plt.figure().add_subplot(111)
    x = arange(0, n, 1)
    y = result
    ax.plot(x, y)

    plt.show()  