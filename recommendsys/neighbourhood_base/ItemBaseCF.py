# coding=utf-8
import math


def ItemSimilarity(train):
    """compute item similarity matrix
    :param train:
    :return:
    """
    # calculate co-rated users between items
    C = dict()
    N = dict()  ##number of users
    for u, items in train.items():
        item = items.keys()
        for i in item:
            if (not N.has_key(i)):
                N.setdefault(i, 0)
            N[i] += 1
            for j in item:
                if i == j:
                    continue
                if (not C.has_key(i)):
                    C.setdefault(i, {})
                if (not C[i].has_key(j)):
                    C[i].setdefault(j, 0)
                C[i][j] += 1
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


def Recommend(train, user, W, K=3):
    """ use item CF to recommend
    :param train: 嵌套字典结构的训练集
    :param user: 要推荐的对象
    :param W: 相似度矩阵（嵌套字典）
    :param K: 相似度最高的k个物品
    :return:k个物品（包含物品和用户u对物品j的兴趣度）
    """
    rank = dict()
    reason = dict()
    ru = train[user]
    for i, pi in ru.items():
        neighbour = W[i]
        for j, wj in sorted(neighbour.items(), key=lambda p: p[1], reverse=True)[0:K]:
            if j in ru:
                # we should filter items user interacted before
                continue
            if (not rank.has_key(j)):
                rank.setdefault(j, 0)
            reason.setdefault(i, pi * wj)
            rank[j] += pi * wj  ## here pi = 1
    return sorted(rank.items(), key=lambda p: p[1])


_train = {
    "A": {"a": 1, "b": 1, "d": 1},
    "B": {"b": 1, "c": 1, "e": 1},
    "C": {"c": 1, "d": 1},
    "D": {"b": 1, "c": 1, "d": 1},
    "E": {"a": 1, "d": 1}
}
# print(ItemSimilarity(_train))
print(Recommend(_train, "A", ItemSimilarity(_train)))
