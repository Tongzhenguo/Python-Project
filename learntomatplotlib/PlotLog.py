import math

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.arange(0.05,3,0.05)
    y1 = [math.log(a,1.5) for a in x]
    plt.plot(x,y1,linewidth=2,color="#ff0000",label="log1.5(x)")


    y2 = [math.log(a,2) for a in x]
    plt.plot(x,y2,linewidth=2,color="#00ff00",label="log2(x)")

    y3 = [math.log(a,3) for a in x]
    plt.plot(x,y3,linewidth=2,color="#0000ff",label="log3(x)")
    # draw a split line pass a point (1,0)
    plt.plot([1, 1], [y1[0], y1[-1]], "r--", linewidth=2)

    plt.legend(loc="low right")
    plt.grid(True)
    plt.show()