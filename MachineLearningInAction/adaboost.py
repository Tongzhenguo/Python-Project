# coding=utf-8
from numpy import matrix, log, multiply, exp, sign


def loadSimpleData():
    dataMat = matrix([
        [1., 2.1],
        [2., 1.1],
        [1.3, 1.],
        [1., 1.],
        [2., 1.]
    ])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return dataMat, classLabels


# coding=utf-8
###单层决策树的生成
from numpy import ones, shape, mat, zeros, inf


def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    """通过阀值比较对数据进行分类，通过数据过滤来实现
    :param dataMatrix:训练集矩阵
    :param dimen:划分的特征
    :param threshVal:划分的阀值
    :param threshIneq:大于还是小于等于
    :return:类别数组
    """
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0
    return retArray


def bulidStump(dataArr, classLabels, D):
    """基于权重向量D构造的数据集，找到最佳单层决策树
    :param dataArr: 训练集数组
    :param classLabels: 类别标签
    :param D: 权重向量
    :return: 最佳单层决策树(错误率低)，错误率，类别估计值
    """
    dataMatrix = mat(dataArr)
    labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClassEst = mat(zeros((m, 1)))
    minError = inf  ##正无穷大
    for i in range(n):
        rangeMin = dataMatrix[:, i].min()
        rangeMax = dataMatrix[:, i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:  ##在大于和小于之间切换不等式
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = mat(ones((m, 1)))  ##错误分类的计数向量
                errArr[predictedVals == labelMat] = 0
                weightdError = D.T * errArr
                # print "split:dim %d,thresh %.2f,thresh ineqal: %s,the weighted error is %.3f" \
                #       %(i,threshVal,inequal,weightdError)
                if (weightdError < minError):
                    minError = weightdError
                    bestClassEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst


# D = mat(ones( (5,1) ) / 5)
# (datMat,classLabels) = loadSimpleData()
# bulidStump(datMat,classLabels,D)

###基于单层决策树的AdaBoost训练过程
def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    """基于单层决策树的AdaBoost训练过程
    :param dataArr: 训练集数组
    :param classLabels: 标签数组
    :param numIt:迭代次数
    :return: 多个决策树的线性加权组合
    """
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIt):
        bestStump, error, classEst = bulidStump(dataArr, classLabels, D)
        print "D:", D.T
        alpha = float(0.5 * log(1.0 - error) / max(error, 1e-16))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print "classEst : ", classEst.T
        ## 为下一次迭代计算D
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        aggClassEst += alpha * classEst
        print "aggClassEst: ", aggClassEst.T
        aggeErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggeErrors.sum() / m
        print "total error: ", errorRate, "\n"
        if errorRate == 0.0:
            break
    return weakClassArr


(datMat, classLabels) = loadSimpleData()
classifierArray = adaBoostTrainDS(datMat, classLabels, 9)
