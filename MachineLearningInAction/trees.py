# coding=utf-8
from math import log
"""
计算(香农)(信息)熵 ShannonEntropy
"""
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel  = featVec[-1] #倒数第一行
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0 #init counts
        labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        for key in labelCounts:
            prop = float(labelCounts[key]) / numEntries
            shannonEnt -= prop * log(prop,2)
    return shannonEnt
"""
鱼鉴定数据集
"""
def createDateSet():
    dataSet = [
        [1,1,'yes'],
        [1,1,'yes'],
        [1,0,'no'],
        [0,1,'no'],
        [0,1,'no']
    ]
    labels = ['no surfacing','flippers']
    return dataSet,labels #等价于(dataSet,labels)
# myDat,labels = createDateSet()
# print calcShannonEnt(myDat)
# myDat[0][-1] = 'maybe'
# #print myDat
# print calcShannonEnt(myDat)

"""
按照给定特征划分数据集
"""
def splitDataSet(dataSet,axis,value):
    """
    :param dataSet: 原数据集
    :param axis: 特征字段
    :param value: 特征分隔点
    :return: 划分后的数据集
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:]) #去掉特征字段,拼接函数
            retDataSet.append(reducedFeatVec) #
    return retDataSet
# myDat,labels = createDateSet()
# print myDat
# print splitDataSet(myDat,0,1)

def chooseBestFeatureToSplit(dataset):
    numFeatures = len(dataset[0]) -1
    baseEntropy = calcShannonEnt(dataset) #熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset] ##列表生成式
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataset,i,value)
            prob = len(subDataSet)/dataset
            newEntropy += prob * calcShannonEnt(subDataSet) #条件熵
        infoGain = baseEntropy - newEntropy ##信息增益 = 熵- 条件熵
        if(infoGain >bestInfoGain): ##计算最佳信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature