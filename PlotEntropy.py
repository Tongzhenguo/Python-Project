import math
import matplotlib.pyplot as plt

__author__ = 'arachis'

def H(P):
        res = 0
        for p in P:
            res += ( p*math.log(p,math.e) )
        res = -res
        return res

if __name__ == "__main__":
    res = []
    for i in range(1,51,1):
        res.append( H([float(i)/100,1-float(i)/100]) )
    for i in range(51,100,1):
        res.append( H([1-float(i)/100,float(i)/100]) )
    plt.grid(True)
    plt.show()
