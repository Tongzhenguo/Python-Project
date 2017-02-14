import math
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'arachis'

def H(P):
        res = 0
        for p in P:
            res += ( p*math.log(p,math.e) )
        res = -res
        return res


if __name__ == "__main__":
    x = np.linspace(0,1,100)
    # print x
    y = np.empty_like(x)
    for i in range(1,51,1):
        y[i] =  H([float(i)/100,1-float(i)/100])
    for i in range(51,100,1):
        y[i] =  H([1-float(i)/100,float(i)/100])
    # print y
    plt.plot(x,y)
    plt.grid(True)
    plt.show()
