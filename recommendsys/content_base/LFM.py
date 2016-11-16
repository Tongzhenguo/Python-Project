# coding=utf-8
import random


def RandomSelectNegativeSample(self, items, items_pool=None):
    """负样本采样
    采样原则：
    1.对每个用户，要保证正负样本的平衡
    2.对每个用户采样负样本时，要选取那些很热门，而用户却没有行为的物品
    :param self:
    :param items:用户已经有过行为的物品的字典
    :param items_pool:候选物品列表，物品i出现的次数和物品i的流行度成正比
    :return:
    """
    ret = dict()
    for i in items.keys():
        ret[i] = 1
    n = 0
    for i in range(0, len(items) * 3):
        item = items_pool[random.randint(0, len(items_pool) - 1)]
        if (item in ret):
            continue
        ret[item] = 0
        n += 1
        if (n > len(items)):
            break
    return ret


def InitModel(user_items, F):
    """初始化LFM的P,Q
    :param user_items:
    :param F:
    :return:
    """
    pass


def Predict(user, item):
    """根据item的P，Q乘积的和计算预测用户u对物品i的评分
    :param user:
    :param item:
    :return:pui
    """
    pass
def LatentFactorModel(user_items, F, N, alpha, _lambda):
    """实现LFM算法
    :param user_items:
    :param F:隐特征的个数
    :param N:迭代次数
    :param alpha:学习效率
    :param _lambda:正则化参数
    :return:
    """
    [P, Q] = InitModel(user_items, F)
    for step in range(0, N):
        for user, items in user_items.items():
            samples = RandomSelectNegativeSample(items)
            for item, rui in samples.items():
                eui = rui - Predict(user, item)
                for f in range(0, F):
                    P[user][f] += alpha * (eui * Q[item][f] - _lambda * P[item][f])
                    Q[user][f] += alpha * (eui * P[item][f] - _lambda * Q[item][f])
        alpha *= 0.9

    def Recommend(user, P, Q):
        """根据LFM预测用户对物品i的评分
        :param user:
        :param P:
        :param Q:
        :return:
        """
        rank = dict()
        for f, puf in range(0, len(P[user])):
            for i, qfi in Q[f]:
                if i not in rank:
                    rank[i] = Predict(user, i)
        return rank
