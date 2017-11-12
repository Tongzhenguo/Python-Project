# coding=utf-8
from __future__ import print_function

'''
    source:https://people.duke.edu/~ccc14/sta-663/EMAlgorithm.html
'''
import numpy as np
np.set_printoptions(formatter={'all':lambda x: '%.3f' % x})

# xs = np.array([(5,5), (9,1), (8,2), (4,6), (7,3)])
# thetas = np.array([[0.6, 0.4], [0.5, 0.5]])
#
# tol = 0.01
# max_iter = 100
#
# ll_old = 0
# for i in range(max_iter):
#     ws_A = []
#     ws_B = []
#
#     vs_A = []
#     vs_B = []
#
#     ll_new = 0
#
#     # E-step: calculate probability distributions over possible completions
#     for x in xs:
#
#         # multinomial (binomial) log likelihood
#         ll_A = np.sum([x*np.log(thetas[0])])
#         ll_B = np.sum([x*np.log(thetas[1])])
#
#         # [EQN 1]
#         denom = np.exp(ll_A) + np.exp(ll_B)
#         w_A = np.exp(ll_A)/denom
#         w_B = np.exp(ll_B)/denom
#
#         ws_A.append(w_A)
#         ws_B.append(w_B)
#
#         # used for calculating theta
#         vs_A.append(np.dot(w_A, x))
#         vs_B.append(np.dot(w_B, x))
#
#         # update complete log likelihood
#         ll_new += w_A * ll_A + w_B * ll_B
#
#     # M-step: update values for parameters given current distribution
#     # [EQN 2]
#     thetas[0] = np.sum(vs_A, 0)/np.sum(vs_A)
#     thetas[1] = np.sum(vs_B, 0)/np.sum(vs_B)
#     # print distribution of z for each x and current parameter estimate
#
#     print "Iteration: %d" % (i+1)
#     print "theta_A = %.2f, theta_B = %.2f, ll = %.2f" % (thetas[0,0], thetas[1,0], ll_new)
#
#     if np.abs(ll_new - ll_old) < tol:
#         break
#     ll_old = ll_new


def em(xs, thetas, max_iter=100, tol=1e-6):
    '''
    Expectation-maximization for coin sample problem.
    :param xs:输入变量
    :param thetas:隐变量
    :param max_iter:最大迭代次数
    :param tol:最小误差
    :return:
    '''

    ll_new, i = 0,0
    ll_old = -np.infty
    for i in range(max_iter):
        ll = np.array([np.sum(xs * np.log(theta), axis=1) for theta in thetas])
        lik = np.exp(ll)
        ws = lik/lik.sum(0)
        vs = np.array([w[:, None] * xs for w in ws])
        thetas = np.array([v.sum(0)/v.sum() for v in vs])
        ll_new = np.sum([w*l for w, l in zip(ws, ll)])
        if np.abs(ll_new - ll_old) < tol:
            break
        ll_old = ll_new
    return i, thetas, ll_new

if __name__ == "__main__":
    np.random.seed(1234)
    #Example of coin tossing
    n = 100
    p0 = 0.8
    p1 = 0.35
    xs = np.concatenate([np.random.binomial(n, p0, n/2), np.random.binomial(n, p1, n/2)])
    xs = np.column_stack([xs, n-xs])
    np.random.shuffle(xs)
    
    results = [em(xs, np.random.random((2,2))) for i in range(10)]
    i, thetas, ll = sorted(results, key=lambda x: x[-1])[-1]
    print(i)
    for theta in thetas:
        print(theta)
    print(ll)
    