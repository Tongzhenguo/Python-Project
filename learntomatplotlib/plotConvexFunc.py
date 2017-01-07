# coding=utf-8
"""
    绘制二维凸函数 f(x1,x2) = log(exp(x1) + exp(x2))

"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
u = np.linspace(0,4,1000)
x, y = np.meshgrid(u,u)
z = np.log(np.exp(x)+np.exp(y))
ax.contourf(x,y,z,20)
plt.show()