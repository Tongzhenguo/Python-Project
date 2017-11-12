# coding=utf-8
from __future__ import print_function

'''
    source:http://www.bogotobogo.com/python/python_numpy_batch_gradient_descent_algorithm.php
'''

import numpy as np
import random
import sklearn
from sklearn.datasets.samples_generator import make_regression
import pylab
from scipy import stats


def gradient_descent(alpha, x, y, ep=0.0001, max_iter=10000):
    '''
    实现批梯度学习的核心代码，这里用于解决线性回归问题
    :param alpha: 学习率
    :param x: 自变量
    :param y: 目标变量
    :param ep: 最小误差限
    :param max_iter:最大迭代次数
    :return: W,b
    '''
    converged = False
    iter = 0
    m = x.shape[0]  # number of samples

    # initial theta
    t0 = np.random.random(x.shape[1])
    t1 = np.random.random(x.shape[1])

    # total error, J(theta),定义平方损失函数
    J = sum([(t0 + t1 * x[i] - y[i]) ** 2 for i in range(m)])

    # Iterate Loop
    while not converged:
        # for each training sample, compute the gradient (d/d_theta j(theta))
        grad0 = 1.0 / m * sum([(t0 + t1 * x[i] - y[i]) for i in range(m)])
        grad1 = 1.0 / m * sum([(t0 + t1 * x[i] - y[i]) * x[i] for i in range(m)])

        # update the theta_temp
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1

        # update theta
        t0 = temp0
        t1 = temp1

        # mean squared error
        e = sum([(t0 + t1 * x[i] - y[i]) ** 2 for i in range(m)])

        if abs(J - e) <= ep:
            print('Converged, iterations: ', iter, '!!!')
            converged = True

        J = e  # update error
        iter += 1  # update iter

        if iter == max_iter:
            print('Max interactions exceeded!')
            converged = True

    return t0, t1


if __name__ == '__main__':
    ## 构造数据
    x, y = make_regression(n_samples=100, n_features=1, n_informative=1,
                           random_state=0, noise=35)
    print('x.shape = %s y.shape = %s' % (x.shape, y.shape))

    alpha = 0.01  # learning rate
    ep = 0.01  # convergence criteria

    # call gredient decent, and get intercept(=theta0) and slope(=theta1)
    theta0, theta1 = gradient_descent(alpha, x, y, ep, max_iter=1000)
    print('theta0 = %s theta1 = %s' % (theta0, theta1) )

    # check with scipy linear regression
    # slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[:, 0], y)
    # print('intercept = %s slope = %s') % (intercept, slope)

    # plot
    for i in range(x.shape[0]):
        y_predict = theta0 + theta1 * x

    pylab.plot(x, y, 'o')
    pylab.plot(x, y_predict, 'k-')
    pylab.show()
    print("Done!")
