# coding=utf-8
from __future__ import print_function

__autor__ = 'arachis'
__date__ = '2018/5/27'

"""
模拟退火算法:
    1.由来:初始一个种群,每一次迭代会将当前最优解(精英选拔)和余下的部分做部分改变(变异或者交叉配对)
    2.算法步骤:初始化为一组随机解,之后对当前这组解排序,选出最有解和对余下部分做变异或者交叉配对;
        不断如下迭代,直至达到最大迭代次
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


def geneticoptimize(domain, costf, popsize=50, step=1,
                    mutprob=0.2, elite=0.2, maxiter=100):
    """
    遗传算法实现
    :param domain:list,一个由每个人往返航班的最小，最大值二元组构成的列表
    :param costf: func,成本函数
    :param popsize: int,种群大小
    :param step:变化的最大幅度
    :param mutprob:float,种群中变异得来的成员占比
    :param elite:float,种群中精英成员占比
    :param maxiter:int,最大迭代次数
    :return:list,最优解
    """
    def mutate(vec):
        """
        变异操作
        :param vec: list,一个解
        :return: list,变异解
        """
        i = random.randint(0, len(domain) - 1)
        if random.random() < 0.5 and vec[i] > domain[i][0]:
            return vec[0:i] + [vec[i] - step] + vec[i + 1:]
        elif vec[i] < domain[i][1]:
            return vec[0:i] + [vec[i] + step] + vec[i + 1:]

    def crossover(r1, r2):
        """
        交叉操作
        :param r1:list,一个解
        :param r2:list,另一个解
        :return:list,交叉解
        """
        i = random.randint(1, len(domain) - 2)
        return r1[0:i] + r2[i:]

    # 随机初始化种群
    pop = []
    for i in range(popsize):
        vec = [random.randint(domain[i][0], domain[i][1])
               for i in range(len(domain))]
        pop.append(vec)

    # 计算精英群体大小
    topelite = int(elite * popsize)

    # Main loop
    for i in range(maxiter):
        scores = [(costf(v), v) for v in pop]
        scores.sort()
        ranked = [v for (s, v) in scores]

        # 从纯粹的胜出者开始
        pop = ranked[0:topelite]

        # 添加变异或者交叉配对后的解
        while len(pop) < popsize:
            if random.random() < mutprob:

                # Mutation
                c = random.randint(0, topelite)
                pop.append(mutate(ranked[c]))
            else:

                # Crossover
                c1 = random.randint(0, topelite)
                c2 = random.randint(0, topelite)
                pop.append(crossover(ranked[c1], ranked[c2]))

        print(scores[0][0])

    return scores[0][1]

if __name__ == '__main__':
    domain = [(0,9)] * (len(people)*2)
    s = geneticoptimize(domain, schedulecost)
    printschedule(s)