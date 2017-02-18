# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    x = np.array( np.linspace(-3,3,1001,dtype=float) )
    f = x #f = wx+b,这里w=1,b=0
    hinge = 1-f  # loss(y) = max(0 , 1-f )
    hinge[ hinge<0 ] = 0
    plt.plot( x,hinge,label = "hinge loss")
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.savefig("hinge.png")
    plt.show()