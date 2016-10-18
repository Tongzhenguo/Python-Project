# coding=utf-8
from numpy import *
def loadDatasSet(filename):
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
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0],:][0]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0],:][0]
    return mat0,mat1
def regLeaf(dataSet):
    return mean(dataSet)
def regErr(dataSet):
    """计算总方差
    :param dataSet:
    :return:
    """
    return var(dataSet[:,-1]) * shape(dataSet)[0]

def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
    """函数要完成两件事：选择最佳分割，生成相应的叶结点
    :param dataSet:数据集
    :param leafType:叶结点类型，默认是回归叶
    :param errType:划分指标的计算方式，默认是总方差
    :param ops:用户东一的参数构成的元组
    :return:
    """
    tolS = ops[0]
    tolN = ops[1]
    if(len(set(dataSet[:,-1].T.tolist()[0] == 1))):
        return  None,leafType(dataSet)
    m,n = shape(dataSet)
    S = errType
    bestS = inf
    beatIndex = 0
    bestValue = 0
    for featIndex in range(n-1):
        for splitVal in set(dataSet[:,featIndex]):
            mat0,mat1 = binSplitDataSet(dataSet,featIndex,splitVal)
            if(shape(mat0)[0] <tolN or shape(mat1)[0] <tolN):
                continue
            newS = errType(mat0) + errType(mat1)
            if(newS < bestS):
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    if(S - bestS) < tolS:
        return None,leafType
    mat0,mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    if(shape(mat0)[0] <tolN or shape(mat0)[0] <tolN):
        return None,leafType(dataSet)
    return bestIndex,bestValue


def createTree(dataSet,leafType,errType,ops=(1,4)):
    """递归创建决策树
    :param dataSet:数据集
    :param leafType:叶子类型，回归树是是一个常数，模型树是一个线性方程
    :param errType:误差计算函数
    :param ops:包含树构建所需其他参数的元组
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
testMat = mat(eye(4))
mat0,mat1 = binSplitDataSet(testMat,1,0.5)
print((mat0,mat1))