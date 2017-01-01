# coding=utf-8
import math

import matplotlib.pyplot as plt

"""
    plot 函数学习：
    color:http://matplotlib.org/api/colors_api.html
    marker:http://matplotlib.org/api/markers_api.html

    附：
    颜色： 蓝色 - 'b' 绿色 - 'g' 红色 - 'r' 青色 - 'c' 品红 - 'm' 黄色 - 'y' 黑色 - 'k'（'b'代表蓝色，所以这里用黑色的最后一个字母） 白色 - 'w'
    线： 直线 - '-' 虚线 - '--' 点线 - ':' 点划线 - '-.'
    常用点标记 点 - '.' 像素 - ',' 圆 - 'o' 方形 - 's' 三角形 - '^'
"""

if __name__ == "__main__":
    x = [float(i)/100.0 for i in range(1,300)]
    y = [math.log(i) for i in x]
    plt.plot(x,y,'r-',linewidth=3,label='log Curve') # 这里的-代表连续的直线
    a = [x[20],x[175]]
    b = [y[20],y[175]]
    plt.plot(a,b,'g--',linewidth=2) ##default color
    plt.plot(a,b,'b^',markersize=15,alpha=1) #blue star and opaque(不透明)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('log(X)')
    plt.show()