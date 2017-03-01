# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib as mpl
import matplotlib.colors
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances_argmin

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

iris_feature = u'花萼长度', u'花萼宽度', u'花瓣长度', u'花瓣宽度'


def expand(a, b, rate=0.05):
    d = (b - a) * rate
    return a-d, b+d


def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]


if __name__ == '__main__':
    path = 'F:\code\Python-Project\dataset\iris\\10.iris.data'
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    # 将数据的0到3列组成x，第4列得到y
    x_prime, y = np.split(data, (4,), axis=1)
    y = y.ravel()

    n_components = 3
    feature_pairs = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    plt.figure(figsize=(10, 9), facecolor='#FFFFFF')
    for k, pair in enumerate(feature_pairs):
        x = x_prime[:, pair]
        m = np.array([np.mean(x[y == i], axis=0) for i in range(3)])  # 均值的实际值
        print '实际均值 = \n', m

        gmm = GaussianMixture(n_components=n_components, covariance_type='full', random_state=0)
        gmm.fit(x)
        print '预测均值 = \n', gmm.means_
        print '预测方差 = \n', gmm.covariances_
        y_hat = gmm.predict(x) #Compute minimum distances between one point and a set of points.
        order = pairwise_distances_argmin(m, gmm.means_, axis=1, metric='euclidean')
        print '顺序：\t', order #标记分类

        n_sample = y.size
        n_types = 3
        change = np.empty((n_types, n_sample), dtype=np.bool)
        for i in range(n_types):
            change[i] = y_hat == order[i]
        for i in range(n_types):
            y_hat[change[i]] = i
        acc = u'准确率：%.2f%%' % (100*np.mean(y_hat == y))
        print acc

        cm_light = mpl.colors.ListedColormap(['#FF8080', '#77E0A0', '#A0A0FF'])
        cm_dark = mpl.colors.ListedColormap(['r', 'g', '#6060FF'])
        x1_min, x1_max = x[:, 0].min(), x[:, 0].max()
        x2_min, x2_max = x[:, 1].min(), x[:, 1].max()
        x1_min, x1_max = expand(x1_min, x1_max)
        x2_min, x2_max = expand(x2_min, x2_max)
        x1, x2 = np.mgrid[x1_min:x1_max:500j, x2_min:x2_max:500j]
        grid_test = np.stack((x1.flat, x2.flat), axis=1)
        grid_hat = gmm.predict(grid_test)

        change = np.empty((n_types, grid_hat.size), dtype=np.bool)
        for i in range(n_types):
            change[i] = grid_hat == order[i]
        for i in range(n_types):
            grid_hat[change[i]] = i

        grid_hat = grid_hat.reshape(x1.shape)
        plt.subplot(3, 2, k+1)
        plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)
        plt.scatter(x[:, 0], x[:, 1], s=30, c=y, marker='o', cmap=cm_dark, edgecolors='k')
        xx = 0.95 * x1_min + 0.05 * x1_max
        yy = 0.1 * x2_min + 0.9 * x2_max
        plt.text(xx, yy, acc, fontsize=14)
        plt.xlim((x1_min, x1_max))
        plt.ylim((x2_min, x2_max))
        plt.xlabel(iris_feature[pair[0]], fontsize=14)
        plt.ylabel(iris_feature[pair[1]], fontsize=14)
        plt.grid()
    plt.tight_layout(2)
    plt.suptitle(u'EM算法无监督分类鸢尾花数据', fontsize=20)
    plt.subplots_adjust(top=0.92)
    plt.show()
