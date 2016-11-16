# coding=utf-8
import math


def RMSE(records):
    """平均标准误差
    :param records:存放用户评分数据，且records[i] = [u,i,rui,pui]
    :return:
    """
    return math.sqrt(sum([(rui - pui) ** 2 for u, i, rui, pui in records]) / float(len(records)))


def MAE(records):
    """
    :param records:
    :return:
    """
    return sum([abs(rui - pui) for u, i, rui, pui in records]) / float(len(records))


def PrecisionRecall(test, N, Recommend=None):
    """
    :param test:测试集
    :param N: 推荐物品个数
    :param Recommend:推荐模型算法
    :return:准确率和召回率
    """
    hit = 0
    n_recall = 0
    n_precision = 0
    for user, items in test.items():
        rank = Recommend(user, N)
        hit += len(rank & items)
        n_recall += len(items)
        n_precision += N
    return [hit / (1.0 * n_recall), hit / (1.0 * n_precision)]
