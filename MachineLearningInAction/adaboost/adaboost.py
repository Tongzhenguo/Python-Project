# coding=utf-8
from numpy import matrix, log, multiply, exp, sign, array
from numpy import ones, shape, mat, zeros, inf

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


def buildStump(dataArr, classLabels, D):
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
# print bulidStump(datMat,classLabels,D)

###基于单层决策树的AdaBoost训练过程
def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    """基于单层决策树的AdaBoost训练过程
    :param dataArr: 训练集数组
    :param classLabels: 标签数组
    :param numIt:迭代次数
    :return: 多个决策树的线性加权组合

    对每次迭代：
    利用bulidStump()函数找到最佳的单层决策树
    将最佳单层决策树加入到单层决策树数组
    计算alpha
    计算新的权重向量D
    更新累计类别估计值
    如果错误率等于0.0,则退出循环
    """

    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))  ##记录每个每个数据点的类别估计累计值
    for i in range(numIt):
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)  ##计算权重向量
        # print "D:", D.T
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))  ##计算该分类器的权重
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        #print "classEst : ", classEst.T
        ## 为下一次迭代计算D
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        aggClassEst += alpha * classEst
        #print "aggClassEst: ", aggClassEst.T
        aggeErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggeErrors.sum() / m
        print "total error: ", errorRate, "\n"
        if errorRate == 0.0:
            break
    # return weakClassArr
    return weakClassArr, aggClassEst

# (datMat, classLabels) = loadSimpleData()
# classifierArray = adaBoostTrainDS(datMat, classLabels, 9)
# print classifierArray
def adaClassify(datToClass, classifierArr):
    """AdaBoost分类函数
    各个分类器的类别估计乘上alpha值的和，取符号函数
    :param datToClass:待分类样例
    :param classifierArr:弱分类器数组
    :return:正负分类标记
    """
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'],
                                 classifierArr[i]['thresh'],
                                 classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha'] * classEst
        # print aggClassEst
    return sign(aggClassEst)


# (datMat, classLabels) = loadSimpleData()
# classifierArray = adaBoostTrainDS(datMat, classLabels, 9)
# print adaClassify([0,0],classifierArray)

def loadDataSet(filename):
    """自适应数据加载函数
    假定最后列是类别标签
    :param filename: 数据文件的文件路径
    :return:
    """


def loadDataSet(fileName):  # general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t'))  # get number of fields
    dataMat = [];
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat - 1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


# datArr, labelArr = loadDataSet('F:\code\Python-Project\dataset\horseColicTraining2.txt')
# classifierArray = adaBoostTrainDS(datArr, labelArr, 10)
# ###
# testArr,testLabelArr = loadDataSet('F:\code\Python-Project\dataset\horseColicTest2.txt')
# prediction10 = adaClassify(testArr,classifierArray)
# errArr = mat(ones( (67,1) ))
# print errArr[prediction10!=mat(testLabelArr).T].sum()

def plotROC(predStrengths, classLabels):
    """ROC曲线的绘制和AUC计算函数
    :param predStrengths:
    :param classLabels:
    :return:
    """
    import matplotlib.pyplot as plt
    cur = (1.0, 1.0)  # cursor
    ySum = 0.0  # variable to calculate AUC
    numPosClas = sum(array(classLabels) == 1.0)
    yStep = 1 / float(numPosClas);
    xStep = 1 / float(len(classLabels) - numPosClas);
    sortedIndicies = predStrengths.argsort()  # get sorted index, it's reverse
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    # loop through all the values, drawing a line segment at each point
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delX = 0;
            delY = yStep;
        else:
            delX = xStep;
            delY = 0;
            ySum += cur[1]
        # draw line from cur to (cur[0]-delX,cur[1]-delY)
        ax.plot([cur[0], cur[0] - delX], [cur[1], cur[1] - delY], c='b')
        cur = (cur[0] - delX, cur[1] - delY)
    ax.plot([0, 1], [0, 1], 'b--')
    plt.xlabel('False positive rate');
    plt.ylabel('True positive rate')
    plt.title('ROC curve for AdaBoost horse colic detection system')
    ax.axis([0, 1, 0, 1])
    plt.show()
    print "the Area Under the Curve is: ", ySum * xStep


datArr, labelArr = loadDataSet('F:\code\Python-Project\dataset\horseColicTraining2.txt')
classifierArray, aggClassEst = adaBoostTrainDS(datArr, labelArr, 10)
plotROC(aggClassEst, labelArr)
