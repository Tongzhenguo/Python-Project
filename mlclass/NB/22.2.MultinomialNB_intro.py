#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB


if __name__ == "__main__":
    np.random.seed(0)
    M = 200
    N = 1000
    x = np.random.randint(2, size=(M, N))     # [low, high)
    x = np.array(list(set([tuple(t) for t in x])))
    M = len(x)
    # y = np.arange(M)
    y = [0, 1, 2] * (int)((float(M)/3)+1)
    y = np.array(y[0:M])
    print '样本个数：%d，特征数目：%d' % x.shape
    print '样本：\n', x
    mnb = MultinomialNB(alpha=1)    # 动手：换成GaussianNB()试试预测结果？
    mnb.fit(x, y)
    y_hat = mnb.predict(x)
    print '预测类别：', y_hat
    print '准确率：%.2f%%' % (100*np.mean(y_hat == y))
    print '系统得分：', mnb.score(x, y)
    # from sklearn import metrics
    # print metrics.accuracy_score(y, y_hat)
    # err = y_hat != y
    # for i, e in enumerate(err):
    #     if e:
    #         print y[i], '：\t', x[i], '被认为与', x[y_hat[i]], '一个类别'
