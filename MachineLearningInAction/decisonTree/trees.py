# coding=utf-8
from math import log
import operator

from MachineLearningInAction.decisonTree import treePlotter

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
        featList = [example[i] for example in dataset] ##列表生成式，list comprehension
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataset,i,value)
            prob = float(len(subDataSet))/len(dataset)
            newEntropy += prob * calcShannonEnt(subDataSet) #条件熵
        infoGain = baseEntropy - newEntropy ##信息增益 = 熵- 条件熵
        if(infoGain >bestInfoGain): ##计算最佳信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
# myDat,labels = createDateSet()
# print chooseBestFeatureToSplit(myDat)
def majorityCnt(classList):
    """多数表决叶子节点的分类
    :param classList:分类列表
    :return:分类标签
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] +=1
        ##Return a callable object that fetches the given item(s) from its operand.
        ### 字典的value作为排序的key,降序排列
        sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter[1],reverse=True)
    return sortedClassCount[0][0]
def createTree(dataset,labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0] ##全是同一类
    if(len(dataset[0]) == 1):
       return majorityCnt(classList)## 只剩下一个特征
    ### 如果都不是，则选择最佳特征
    bestFeat = chooseBestFeatureToSplit(dataset)
    bestFeatureLabel = labels[bestFeat]
    ##将树存储在嵌套字典中
    myTree = {bestFeatureLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    ##遍历最佳特征的所有取值
    for value in uniqueVals:
        subLabels = labels[:] ##如果直接赋值labels呢？不行，python的函数参数是引用传递
        myTree[bestFeatureLabel][value] = createTree(splitDataSet(dataset,bestFeat,value),subLabels)
    return myTree
def classify(inputTree,featLabels,testVec):
    """预测样本的分类
    :param inputTree:训练得到的用嵌套字典表示的决策树
    :param featLabels: 特征向量
    :param testVec: 预测向量
    :return: 分类标签
    """
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    ##找到划分特征所在的索引
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if(testVec[featIndex] == key):
            if(type(secondDict[key]).__name__ == 'dict'):
                ## python没有局部变量的概念，只有class,def能改变作用域
                classLabel = classify(secondDict[key],featLabels,testVec)
            else:
                classLabel = secondDict[key]
            return classLabel
def storeTree(inputTree,filename):
    """将训练后的模型序列化(使用pickle)到磁盘中
    :param inputTree: 以嵌套字典表示的决策树
    :param filename: 保存文件
    :return:
    """
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
def grabTree(filename):
    """从文件中加载决策树（反序列化）
    :param filename:
    :return: 表示决策树模型的嵌套字典对象
    """
    import pickle
    fr = open(filename)
    return pickle.load(fr)
# myTree = treePlotter.retrieveTree(0)
# storeTree(myTree,'DescionTreeModel.txt')
print grabTree('DescionTreeModel.txt')
# myDat,labels = createDateSet()
# print classify(myTree,labels,[1,0])
# print createTree(myDat,labels)
