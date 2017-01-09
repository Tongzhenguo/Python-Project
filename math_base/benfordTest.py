# coding=utf-8
"""
        问：统计出从1! 到 N！（N为正整数）的所有数中，首位数字是k(k=1,2,...,9)的概率

"""

import matplotlib.pyplot as plt
def first_digital(x):
    while x >= 10:
        x /= 10
    return x

if __name__ == "__main__":
    n = 1
    frequency = [0] * 9
    for i in range(1,1000):
        n *= i
        m = first_digital(n) - 1
        frequency[m] += 1
    print frequency
    for x,y in enumerate(frequency):
        plt.text(x+1.1, y, frequency[x], verticalalignment='top', fontsize=15)
    plt.plot(frequency,'r-',linewidth=2)
    plt.plot(frequency, 'go', markersize=8)
    plt.grid(True)
    plt.show()












