# coding=utf-8
from __future__ import print_function

__autor__ = 'arachis'
__date__ = '2018/5/27'

"""
模拟退火算法:
    1.由来:退火是指将合金加热后再慢慢冷却的过程,大量的原子会逐渐找到一个稳态。
    2.算法步骤:初始化为一个随机解,之后会不断以p = e^(-(highcost-lowcost)/tmperature)的概率
        接受较差的解,随着迭代次数增加,温度越来越低,如果成本的差异越大,解被选择的概率就越低
"""
import time
import random
import math

people = [('Seymour', 'BOS'),
          ('Franny', 'DAL'),
          ('Zooey', 'CAK'),
          ('Walt', 'MIA'),
          ('Buddy', 'ORD'),
          ('Les', 'OMA')]

# 纽约的Laguardia机场
destination = 'LGA'

# 构建flights字典,其起止点为key,其航班详情为value
flights = {}
for line in file('schedule.txt'):
    origin, dest, depart, arrive, price = line.strip().split(',')
    flights.setdefault((origin, dest), [])

    # Add details to the list of possible flights
    flights[(origin, dest)].append((depart, arrive, int(price)))


def getminutes(t):
    """
    计算某个给定时间在一天的分钟数
    :param t:str,时间字符串
    :return:int,分钟数
    """
    x = time.strptime(t, '%H:%M')
    return x[3] * 60 + x[4]


def printschedule(r):
    """
    打印航班
    :param r:数字列表标识的航班序列
    :return:None
    """
    for d in range(len(r)/2):
        name=people[d][0]
        origin=people[d][1]
        out=flights[(origin,destination)][int(r[d])]
        ret=flights[(destination,origin)][int(r[d+1])]
        print('%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin,
                                                      out[0], out[1], out[2],
                                                      ret[0], ret[1], ret[2]))


def schedulecost(sol):
    """
    定义成本函数
    :param sol:list,搭乘航班列表
    :return:int,总成本值
    """
    totalprice = 0
    latestarrival = 0
    earliestdep = 24 * 60

    for d in range(len(sol) / 2):
        # 得到往返航班
        origin = people[d][1]
        outbound = flights[(origin, destination)][int(sol[d])]
        returnf = flights[(destination, origin)][int(sol[d + 1])]

        # 总价格等于所有往返航班价格之和
        totalprice += outbound[2]
        totalprice += returnf[2]

        # 记录最晚到达时间和最早离开时间
        if latestarrival < getminutes(outbound[1]): latestarrival = getminutes(outbound[1])
        if earliestdep > getminutes(returnf[0]): earliestdep = getminutes(returnf[0])

    # 每个人必须在机场等待直到最后一个人到达为止
    # 他们也必须在相同时间到达，并等候他们的返程航班
    totalwait = 0
    for d in range(len(sol) / 2):
        origin = people[d][1]
        outbound = flights[(origin, destination)][int(sol[d])]
        returnf = flights[(destination, origin)][int(sol[d + 1])]
        totalwait += latestarrival - getminutes(outbound[1])
        totalwait += getminutes(returnf[0]) - earliestdep

    # 是否需要付罚款
    if latestarrival > earliestdep: totalprice += 50

    return totalprice + totalwait


def annealingoptimize(domain, costf, T=10000.0, cool=0.95, step=1):
    """
    实现模拟退化算法
    :param domain:list,一个由每个人往返航班的最小，最大值二元组构成的列表
    :param costf: func,成本函数
    :param T:初始温度
    :param cool:冷却速度
    :param step:最远方向的步长
    :return:list,最优解
    """
    # 随机初始化值
    vec = [float(random.randint(domain[i][0], domain[i][1]))
           for i in range(len(domain))]

    while T > 0.1:
        # 选择一个索引值
        i = random.randint(0, len(domain) - 1)

        # 选择一个改变索引值的方向
        dir = random.randint(-step, step)

        # 创建一个代表题解的新列表,改变其中一个值
        vecb = vec[:]
        vecb[i] += dir
        if vecb[i] < domain[i][0]:
            vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]

        # 计算当前成本和新成本
        ea = costf(vec)
        eb = costf(vecb)
        p = pow(math.e, (-eb - ea) / T)

        # 判断是否选择这个解
        if (eb < ea or random.random() < p):
            vec = vecb

        # 降低温度
        T = T * cool
    return vec


if __name__ == '__main__':
    domain = [(0,9)] * (len(people)*2)
    s = annealingoptimize(domain, schedulecost)
    print( schedulecost(s) )
    printschedule(s)