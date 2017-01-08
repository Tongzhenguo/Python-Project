# coding=utf-8
"""
    使用泰勒公式计算指数函数e^x：
        对给定正整数x,可以分解 x = k * ln2 + r,k是正整数，r是小数
        经过换底得e ** x = 2 ** k * e ** r
    e ** x的泰勒公式如下：
        e**x = 1 + x + x**2/2! + x**3/3! + ... + x**n/n! + Rn
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def calc_e_small(x):
    n = 10
    f = np.arange(1,n+1).cumprod() #求累乘(the cumulative product)
    b = np.array([x]*n).cumprod()
    return np.sum(b/f)+1

def calc_e(x):
    reverse = False
    if(x<0):
        x = -x #处理负数
        reverse = True
    ln2 = 0.69314718055994530941723212145818
    c = x / ln2
    k = int(c+0.5)
    r = x - k*ln2
    y = 2**k * calc_e_small(r)
    if reverse:
        return 1/y
    return y

if __name__ == "__main__":
    t1 = np.linspace(-2,0,10,endpoint=False)
    t2 = np.linspace(0,2,20)
    t = np.concatenate((t1,t2))
    print(t) ## 横轴数据
    y = np.empty_like(t) ## 产生相同个数的0
    for i,x in enumerate(t):
        y[i] = calc_e(x)
        print "e^",x,' = ',y[i],'(近似值)\t',math.exp(x)
    plt.plot(t,y,'r-',t,y,'go',linewidth=2)
    plt.title("Taylor", fontsize=18)
    plt.xlabel('x',fontsize=15)
    plt.ylabel('exp(x)',fontsize=15)
    plt.grid(True)
    plt.show()