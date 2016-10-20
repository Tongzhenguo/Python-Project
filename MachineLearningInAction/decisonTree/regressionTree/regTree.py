# coding=utf-8
from numpy import *

from MachineLearningInAction.decisonTree import treePlotter


def loadDataSet(filename):
    """从文件中加载数据集
    :param filename:文件路径
    :return:二重数组，即矩阵
    """
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)##将每行的内容转成一组浮点数
        dataMat.append(fltLine)
    return dataMat
def binSplitDataSet(dataSet,feature,value):
    """将给定数据集按特征和特征值划分为成两个子数据集
    :param dataSet: 带划分数据集
    :param feature: 划分特征
    :param value: 划分特征值
    :return: 两个数据集的元组
    """
    ## 取出dataSet矩阵的feature列，以value值分割为两部分
    ##nonzero() 的参数是一个数组（array）,返回的是一个非零索引数组(元素还是tuple)和零的索引数组的tuple,(array([1], dtype=int64), array([0], dtype=int64))
    ##dataSet[nonzero(dataSet[:, feature] > value)[0],:][0] 过滤出特征值大于value的数据
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0],:]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0],:]
    return mat0,mat1
def regLeaf(dataSet):
    """返回数据集的平均值
    :param dataSet:
    :return:
    """
    return mean(dataSet)
def regErr(dataSet):
    """计算总误差
    shape()返回矩阵的行列数的元组，var()计算平均误差
    :param dataSet:
    :return:
    """
    return var(dataSet[:,-1]) * shape(dataSet)[0]

def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
    """函数要完成两件事：选择最佳分割，生成相应的叶结点
    :param dataSet:数据集
    :param leafType:叶结点类型，默认是回归叶，叶结点以均值标记
    :param errType:划分指标的计算方式，默认是总误差
    :param ops:用户定义的参数构成的元组，来指定停止条件，一个是最小误差下降值，一个是最少样本数
    :return:最佳划分（bestIndex,bestValue）或者叶结点（None,leafType(dataSet)）
    """
    tolS = ops[0]##误差阀值
    tolN = ops[1]##划分的最少样本数
    ## T是矩阵的转置
    ## 不同剩余特征值的数目，如果数目为一，无需分割成两个子集
    if(len(set(dataSet[:,-1].T.tolist()[0])) == 1):
        return  None,leafType(dataSet)
    m,n = shape(dataSet)##矩阵的行列数s
    S = errType(dataSet)
    bestS = inf##默认为最大值
    bestIndex = 0
    bestValue = 0
    for featIndex in range(n-1):
        ## mat[:,i].T.tolist()[0] 是取矩阵的第i列转置成行向量，再转成list结构，list[0]就是这个行向量，set将指定list去重
        for splitVal in set(dataSet[:,featIndex].T.tolist()[0]):
            mat0,mat1 = binSplitDataSet(dataSet,featIndex,splitVal)
            ## 当划分子集小于最少样本数，跳过
            if(shape(mat0)[0] <tolN or shape(mat1)[0] <tolN):
                continue
            ## 计算最佳分割，计算的标准是左右子集的误差和最小，就是不确定性越低
            newS = errType(mat0) + errType(mat1)
            if(newS < bestS):
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    ##误差下降小于阀值，生成叶结点
    if(S - bestS) < tolS:
        return None,leafType(dataSet)
    ##划分子集小于最少样本数，生成叶结点
    mat0,mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    if(shape(mat0)[0] <tolN or shape(mat1)[0] <tolN):
        return None,leafType(dataSet)
    return bestIndex,bestValue


def createTree(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    """递归创建决策树
    :param dataSet:数据集
    :param leafType:叶子类型，回归树是是一个常数，模型树是一个线性方程
    :param errType:误差计算函数
    :param ops:包含树构建所需其他参数的元组，指定停止条件，一是下降阀值，二是子集最少样本数
    :return:决策树
    """
    feat,val = chooseBestSplit(dataSet,leafType,errType,ops)
    if(feat == None):
        return val
    regTree = {}
    regTree['spInd'] = feat
    regTree['spVal'] = val
    lSet,rSet = binSplitDataSet(dataSet,feat,val)
    regTree['left'] = createTree(lSet,leafType,errType,ops)
    regTree['right'] = createTree(rSet, leafType, errType, ops)
    return regTree
#myDat = loadDatasSet('F:\code\Python-Project\dataset\ex00.txt')
# myDat = loadDatasSet('F:\code\Python-Project\dataset\ex0.txt')
# myDat = loadDatasSet('F:\code\Python-Project\dataset\ex2.txt')
# myMat = mat(myDat)
# print createTree(myMat)
## 模型复杂度过高的例子，过拟合
# print createTree(myMat,ops=(0,1))
# print createTree(myMat)
##
# print createTree(myMat,ops=(10000,4))

def isTree(obj):
    """判断是否是树
    :param obj:
    :return:
    """
    return (type(obj)).__name__ == 'dict'
def getMean(tree):
    """获取树的均值,对树进行塌陷处理
    :param tree:
    :return:
    """
    if isTree(tree['left']):
        tree['left'] = getMean(tree['left'])
    if isTree(tree['right']):
        tree['right'] = getMean(tree['right'])
    return (tree['left'] + tree['right']) / 2.0
def prune(tree,testData):
    """回归树剪枝
    :param tree:回归树
    :param testData:剪枝所需测试集
    :return:剪枝后的决策树
    """
    ## 没有测试数据则对树进行塌陷处理
    if(shape(testData)[0]) == 0:
        return getMean(tree)
    if(isTree(tree["left"]) or isTree(tree['right'])):
        lSet,rSet = binSplitDataSet(testData,tree['spInd'],tree['spVal'])
    if (isTree(tree["left"])):
        tree['left'] = prune(tree['left'],lSet)
    if (isTree(tree["right"])):
        tree['right'] = prune(tree['right'], rSet)
    ## 如果是叶结点，判断是否需要合并（回缩）
    if(not isTree(tree["left"]) and not isTree(tree["right"])):
        lSet,rSet = binSplitDataSet(testData,tree['spInd'],tree['spVal'])
        errorNoMerge = sum(power(lSet[:,-1] - tree['left'],2)) + sum(power(rSet[:,-1] - tree['right'],2))
        treeMean = (tree["left"] + tree["right"]) / 2
        treeMean = sum(power(testData[:,-1] - treeMean,2))
        errorMerge = sum(power(testData[:,-1] - treeMean,2))
        if(errorMerge<errorNoMerge):
            print  "merging"
            return treeMean
        else:
            return tree
    return tree
myDat = loadDataSet('F:\code\Python-Project\dataset\ex0.txt')
myMat = mat(myDat)
myTree =  createTree(myMat,ops=(0,1))
myDatTest = loadDataSet('F:\code\Python-Project\dataset\ex2test.txt')
myMat2Test=mat(myDatTest)
print prune(myTree,myMat2Test)

























