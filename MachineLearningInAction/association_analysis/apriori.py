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


# dataSet = loadDataSet()
# C1 = createcC1(dataSet)  ##1项集
# D = map(set, dataSet)  ##构建集合表示的数据集
# L1, supportData0 = scanD(D, C1, 0.5)  ##1频繁项集
# print L1

def aprioriGen(Lk, k):
    """创建k项集
    python中集合的并对应操作符|
    :param Lk:k-1频繁项集列表
    :param k:项集元素个数
    :return:新的K项集
    """
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2];
            L2 = list(Lk[j])[:k - 2]
            L1.sort();
            L2.sort()
            if L1 == L2:  ##当k-2个项相同时将两个集合合并
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport=0.5):
    """完整的apriori主函数
    :param dataSet:
    :param minSupport:
    :return:
    """
    C1 = createcC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


# dataSet = loadDataSet()
# L,suppData = apriori(dataSet)
# print L
# print L
def rulesFromConseq(freqSet, H, supportData, bigRuleList, minConf=0.7):
    """生成候选规则集合
    :param freqSet:频繁项集
    :param H:后件列表
    :param supportData:支持度数据
    :param bigRuleList:关联规则列表
    :param minConf:最小置信度
    :return:
    """
    m = len(H[0])
    if (len(freqSet) > m + 1):
        Hmp1 = aprioriGen(H, m + 1)  # 尝试进一步合并，创建Hm+1条新候选规则
        Hmp1 = calConf(freqSet, Hmp1, supportData, bigRuleList, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, bigRuleList, minConf)


def calConf(freqSet, H, supportData, bigRuleList, minConf):
    """计算置信度,返回满足置信度的后件的列表
    :param freqSet:频繁项集
    :param H:后件列表
    :param supportData:支持度数据
    :param bigRuleList:关联规则列表
    :param minConf:最小置信度
    :return:满足置信度的后件的列表
    """
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if (conf > minConf):
            print freqSet - conseq, "-->", conseq, "conf", conf
            bigRuleList.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def generateRules(L, supportData, minConf=0.7):
    """关联规则生成函数
    :param L:频繁项集列表
    :param supportData: 支持度数据
    :param minConf: 最小置信度
    :return:
    """
    bigRuleList = []  ##存放规则的列表
    for i in range(1, len(L)):  # 获取两个以上元素的集合
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]  ##H1只包含单个元素集合
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


# dataSet = loadDataSet()
# L,suppData = apriori(dataSet)
# rules= generateRules(L,suppData)
# print rules

mashDataSet = [line.split() for line in open("F:\code\Python-Project\dataset\mushroom.dat").readlines()]
L, suppData = apriori(mashDataSet, 0.3)
for item in L[1]:
    if item.intersection('2'):  # z找出毒蘑菇
        print item
