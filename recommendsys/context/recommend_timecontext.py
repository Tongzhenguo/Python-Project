# coding=utf-8
import math


def RecentPopularity(records, alpha, T):
    """计算物品的流行度
    :param records:输入数据集：用户，物品和时间的三元组
    :param alpha:时间衰减参数
    :param T:给定时间
    :return:物品流行度字典
    """
    ret = dict()
    for user, item, tm in records:
        if (tm >= T):
            continue
        # addToDict( ret,item,1/(1.0 * alpha * (T-tm)) )
        ret.setdefault(item, 1 / (1.0 * alpha * (T - tm)))
    return ret


def ItemSimilarity(train, alpha):
    """compute item similarity matrix
    :param train:训练数据集，用户，物品，时间的三元组
    :param alpha:时间衰减参数
    :return:物品关于时间的相似度
    """
    # calculate co-rated users between items
    C = dict()
    N = dict()  ##number of users
    for u, items in train.items():
        for i, tui in items.items():
            if (not N.has_key(i)):
                N.setdefault(i, 0)
            N[i] += 1
            for j, tuj in items.items():
                if i == j:
                    continue
                if (not C.has_key(i)):
                    C.setdefault(i, {})
                if (not C[i].has_key(j)):
                    C[i].setdefault(j, 0)
                C[i][j] += 1 / (1 + alpha * abs(tui - tuj))
                # print(C)
    # calculate final similarity matrix W
    W = dict()
    for i, related_items in C.items():
        if (not W.has_key(i)):
            W.setdefault(i, {})
        for j, cij in related_items.items():
            if (not W[i].has_key(j)):
                W[i].setdefault(j, 0)
            W[i][j] += cij / math.sqrt(N[i] * N[j])
    return W


def Recommend(train, user, W, K=3, t0=114, alpha=0.8):
    """ use item CF to recommend
    :param train: 嵌套字典结构的训练集
    :param user: 要推荐的对象
    :param W: 相似度矩阵（嵌套字典）
    :param K: 相似度最高的k个物品
    :param t0:当前时间
    :param alpha:时间衰减参数
    :return:k个物品（包含物品和用户u对物品j的兴趣度）
    """
    rank = dict()
    ru = train[user]
    for i, pi in ru.items():
        neighbour = W[i]
        for j, tuj in sorted(neighbour.items(), key=lambda p: p[1], reverse=True)[0:K]:
            if (j in ru.items()):
                continue  # we should filter items user interacted before
            if (not rank.has_key(j)):
                rank.setdefault(j, 0)
        rank[j] += pi * tuj / (1 + alpha * (t0 - tuj))
    return sorted(rank.items(), key=lambda p: p[1], reverse=True)


_train = {
    "A": {"a": 111, "b": 112, "d": 113},
    "B": {"b": 111, "c": 113, "e": 114},
    "C": {"c": 111, "d": 112},
    "D": {"b": 111, "c": 112, "d": 113},
    "E": {"a": 111, "d": 111}
}
# print( ItemSimilarity(_train,0.1) )
item_recommend = Recommend(_train, "A", ItemSimilarity(_train, 0.1))
print(item_recommend)
