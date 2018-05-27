# coding=utf-8
from __future__ import print_function

__autor__ = 'arachis'
__date__ = '2018/5/27'

"""
    集体智慧编程中针对航班选择问题的随机搜索和爬山法的智能算法
"""
import time
import random

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


def randomoptimize(domain, costf):
    """
    随机搜索策略
    :param domain:list,一个由每个人往返航班的最小，最大值二元组构成的列表
    :param costf:func,成本函数
    :return:list,最优解
    """
    best = 999999999
    bestr = None
    for i in range(0, 1000):
        # 创建一个随机解
        r = [float(random.randint(domain[i][0], domain[i][1]))
             for i in range(len(domain))]

        # 计算成本值
        cost = costf(r)

        # 选取当前最优解
        if cost < best:
            best = cost
            bestr = r
    return bestr


def hillclimb(domain, costf):
    """
    爬山法:当前解的下方有一个代价较小的解,则我们就认为
    沿着这个方向走，解会越来越小。
    :param domain:list,一个由每个人往返航班的最小，最大值二元组构成的列表
    :param costf:func,成本函数
    :return:list,最优解
    """
    # 创建一个随机解
    sol = [random.randint(domain[i][0], domain[i][1])
           for i in range(len(domain))]
    # Main loop
    while 1:
        # 创建相邻解的列表
        neighbors = []

        for j in range(len(domain)):
            # 在每个方向相对于原值偏离一点
            if sol[j] > domain[j][0]:
                neighbors.append(sol[0:j] + [sol[j] + 1] + sol[j + 1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j] + [sol[j] - 1] + sol[j + 1:])

        # 在相邻解中寻找最优解
        current = costf(sol)
        best = current
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if cost < best:
                best = cost
                sol = neighbors[j]

        # 如果没有更好的解，则推出循环
        if best == current:
            break
    return sol


if __name__ == '__main__':
    s = [1,4,3,2,7,3,6,3,2,4,5,3]
    printschedule(s)
    '''
    Seymour      BOS  8:04-10:11 $ 95 12:08-14:05 $142
    Franny       DAL 12:19-15:25 $342 10:51-14:16 $256
     Zooey       CAK 10:53-13:36 $189  9:58-12:56 $249
      Walt       MIA  9:15-12:29 $225 16:50-19:26 $304
     Buddy       ORD 16:43-19:00 $246 10:33-13:11 $132
       Les       OMA 11:08-13:07 $175 15:07-17:21 $129
    '''
    print(schedulecost(s))

    domain = [(0,9)] * (len(people)*2)
    s = randomoptimize(domain, schedulecost)
    print( schedulecost(s) )
    printschedule(s)

    s = hillclimb(domain, schedulecost)
    print(schedulecost(s))
    printschedule(s)
