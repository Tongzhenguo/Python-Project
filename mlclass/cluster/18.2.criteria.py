# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
from sklearn import metrics
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

if __name__ == "__main__":
    y = [0, 0, 0, 1, 1, 1]
    y_hat = [0, 0, 1, 1, 2, 2]
    h = metrics.homogeneity_score(y, y_hat)
    c = metrics.completeness_score(y, y_hat)
    print u'同一性(Homogeneity)：', h
    print u'完整性(Completeness)：', c
    v2 = 2 * c * h / (c + h)
    v = metrics.v_measure_score(y, y_hat)
    print u'V-Measure：', v2, v

    print
    y = [0, 0, 0, 1, 1, 1]
    y_hat = [0, 0, 1, 2, 3, 3]
    h = metrics.homogeneity_score(y, y_hat)
    c = metrics.completeness_score(y, y_hat)
    v = metrics.v_measure_score(y, y_hat)
    print u'同一性(Homogeneity)：', h
    print u'完整性(Completeness)：', c
    print u'V-Measure：', v

    # 允许不同值
    print
    y = [0, 0, 0, 1, 1, 1]
    y_hat = [1, 1, 1, 0, 0, 0]
    h = metrics.homogeneity_score(y, y_hat)
    c = metrics.completeness_score(y, y_hat)
    v = metrics.v_measure_score(y, y_hat)
    print u'同一性(Homogeneity)：', h
    print u'完整性(Completeness)：', c
    print u'V-Measure：', v

    y = [0, 0, 1, 1]
    y_hat = [0, 1, 0, 1]
    ari = metrics.adjusted_rand_score(y, y_hat)
    print ari

    y = [0, 0, 0, 1, 1, 1]
    y_hat = [0, 0, 1, 1, 2, 2]
    ari = metrics.adjusted_rand_score(y, y_hat)
    print ari


    #计算畸变程度
    cluster1 = np.random.uniform(0.5, 1.5, (2, 10))
    cluster2 = np.random.uniform(3.5, 4.5, (2, 10))
    X = np.hstack((cluster1, cluster2)).T

    plt.figure()
    plt.axis([0, 5, 0, 5])
    plt.grid(True)
    plt.plot(X[:, 0], X[:, 1], 'k.')

    K = range(1, 10)
    meandistortions = []
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        meandistortions.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

    plt.plot(K, meandistortions, 'bx-')
    plt.xlabel('K')
    plt.ylabel('distortion')
    plt.show()

    """
    计算轮廓系数
    (``a``) and the mean nearest-cluster distance (``b``) for each sample.
    The Silhouette Coefficient for a sample is ``(b - a) / max(a,b)``.
    若SC接近-1，则样本应该被分到别的类，为0样本处于类边界，为1样本分类合理
    """
    x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
    x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
    markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
    subplot_counter = 1

    for t in [2,3,5]:
        subplot_counter = subplot_counter + 1
        plt.subplot(3, 2, subplot_counter)
        kmeans_model = KMeans(n_clusters=t).fit(X)
        for i, l in enumerate(kmeans_model.labels_):
            plt.plot(x1[i], x2[i], color=colors[l], \
                     marker=markers[l], ls='None')
            plt.xlim([0, 10])
            plt.ylim([0, 10])
            plt.title('K=%s, Silhouette Coefficient= %.03f' % (
            t, metrics.silhouette_score(X, kmeans_model.labels_, metric='euclidean')))
    plt.show()