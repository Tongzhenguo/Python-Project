# coding=utf-8
import matplotlib.pyplot as plt
import numpy

"""
    numpy numpy.random.uniform 批量生成动态数组：https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html
    http://codingpy.com/article/a-quick-intro-to-matplotlib/
"""

if __name__ == "__main__":
    times = 10000
    u = numpy.random.uniform(0.0,1.0,times) ## generate a ndarray by uniform distribution
    # plt.hist(u,80,facecolor='g',alpha=0.75)
    # plt.grid(True)
    # plt.show()


    for time in range(times/times):
        u += numpy.random.uniform(0.0,1.0,times)
    u /= times
    plt.hist(u,bins=80,facecolor='g',alpha=0.75)
    plt.grid(True)
    plt.show()
