# coding=utf-8
def loadDataSet():
    """创建一个测试的简单数据集
    :return:
    """
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createcC1(dataSet):
    """创建初始训练集，即1项集(frozenset)
    :param dataSet:
    :return:
    """
    C1 = []
    for transaction in dataSet:
        for item in transaction:  ##python 不能创建只有一个整数的集合，因此这里实现必须使用列表
            if [item] not in C1:  ## C1是1项集的集合
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)  ##对C1中每个项构建一个不变集合


def scanD(D, Ck, minSupport):
    """扫描数据集，返回K频繁项集
    :param D:数据集
    :param Ck:K项集
    :param minSupport:最小支持度
    :return:k频繁项集和频繁项集的支持对
    """
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if (can.issubset(tid)):
                if (not ssCnt.has_key(can)):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems  # 计算所有项集支持度
        if (support >= minSupport):
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


dataSet = loadDataSet()
C1 = createcC1(dataSet)  ##1项集
D = map(set, dataSet)  ##构建集合表示的数据集
L1, supportData0 = scanD(D, C1, 0.5)  ##1频繁项集
print L1
