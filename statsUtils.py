# coding=utf-8
__author__ = 'arachis'

# coding=utf-8
"""
    均值/方差
    偏度/峰度
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def calc(data):
    n = len(data)
    niu,niu2,niu3 = 0.0,0.0,0.0
    for a in data:
        niu += a
        niu2 += a ** 2
        niu3 += a ** 3
    niu,niu2,niu3 = niu/n,niu2/n,niu3/n
    sigma = math.sqrt(niu2 - niu ** 2) ## DX = EX^2 - (EX)^2
    return [niu,sigma,niu3]

def calc_stat(data):
    [niu, sigma, niu3] = calc(data)
    n = len(data)
    niu4 = 0.0
    for a in data:
        a -= niu
        niu4 += a ** 4
    niu4 /= n
    skew = (niu3 - 3*niu*sigma**2 - niu**3) / (sigma ** 3)
    kurt = niu4 / (sigma ** 4)
    return [niu,sigma,skew,kurt]

def calc_statistics(x):
    n = x.shape[0]

    m,m2,m3,m4 = 0,0,0,0
    for t in x:
        m += t
        m2 += t ** 2
        m3 += t ** 3
        m4 += t ** 4
    m,m2,m3,m4 = m/n,m2/n,m3/n,m4/n
    mu,sigma = m,np.sqrt(m2-m ** 2)
    skew = (m3 - 3 * mu * m2 + 2 * mu ** 3) / sigma ** 3
    kurt = (m4 - 4*mu*m3 +6*mu*mu*m2 - 4*mu**3*mu+mu**4) / sigma**4 - 3
    print '手动过计算均值、标准差、偏度、峰度：',mu,sigma,skew,kurt


if __name__ == "__main__":
    num = 10000
    data = list(np.random.randn(num))
    data2 = list(2 * np.random.randn(num))
    data3 = [x for x in data if x > -0.5]
    data4 = list(np.random.uniform(0, 4, num))
    [niu,sigma,skew,kurt] = calc_stat(data)
    [niu2, sigma2, skew2, kurt2] = calc_stat(data2)
    [niu3, sigma3, skew3, kurt3] = calc_stat(data3)
    [niu4, sigma4, skew4, kurt4] = calc_stat(data4)
    print niu,sigma,skew,kurt
    print niu2, sigma2, skew2, kurt2
    print niu3, sigma3, skew3, kurt3
    print niu4, sigma4, skew4, kurt4

    info = r"$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f\ kurt=%.2f$" %(niu,sigma,skew,kurt)
    info2 = r"$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f\ kurt=%.2f$" % (niu2, sigma2, skew2, kurt2)
    plt.text(1,0.38,info,bbox=dict(facecolor='red',alpha=0.25))
    plt.text(1, 0.35, info2, bbox=dict(facecolor='green', alpha=0.25))
    plt.hist(data,30,normed=True,facecolor='r',alpha=0.9)
    plt.hist(data2, 60, normed=True, facecolor='g', alpha=0.8)
    plt.grid(True)
    plt.show()

