# coding=utf-8
import numpy
from sklearn.tree import DecisionTreeRegressor

__author__ = 'arachis'

import numpy
import matplotlib.pyplot as plot
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
import random
'''
   第一步：构造合成数据
'''
#建立一个1000数据的测试集
nPoints = 1000

#x的取值范围：-0.5～+0.5的nPoints等分
xPlot = [-0.5+1/nPoints*i for i in range(nPoints + 1)]

#y值：在x的取值上加一定的随机值或者叫噪音数据
#设置随机数算法生成数据时的开始值，保证随机生成的数值一致
numpy.random.seed(1)
##随机生成宽度为0.1的标准正态分布的数值
##上面的设置是为了保证numpy.random这步生成的数据一致
y = [s + numpy.random.normal(scale=0.1) for s in xPlot]


'''
   第二步：构造训练集和测试集-->随机抽取30%作为测试集，其余70%作为训练集
'''
##测试集大小
nSample = int(nPoints * 0.30)
##在0～npoints直接随机生成nSample个点
idxTest = random.sample(range(nPoints), nSample)
#定义训练集和测试集标签
xTrain = []  #训练集
xTest = []   #测试集
yTrain = []  #训练集标签
yTest = []   #测试集标签
##划分数据
for i in range(nPoints):
    if i not in idxTest:
        xTrain.append(xPlot[i])
        yTrain.append(y[i])
    else :
        xTest.append(xPlot[i])
        yTest.append(y[i])

'''
   第三步：构建模型列表，即：集合方法
   核心思路：
   1）初始化残差列表
   2）在循环中
      a）计算残差
      b）使用残差拟合新回归树
      c）更新残差
   3）获得模型列表
'''
##初始化产生的最大二元决策树的数量
numTreesMax = 30

##树的深度---这个是需要不断调整的
treeDepth = 5

##模型列表：二元决策树列表
modelList = []
##预测值列表
predList = []
##步长，使函数可以更快的收敛:调整eps值，使均方误差最小值在或者接近图右侧
eps = 0.1

#初始化残差函数：由于初始化时预测值为空，所以是实际值
residuals = list(yTrain)
##开始生成模型列表
for iTrees in range(numTreesMax):
    ##添加新二元决策树到模型列表
    modelList.append(DecisionTreeRegressor(max_depth=treeDepth))
    ##通过最新的二元决策树拟合数据
    modelList[-1].fit(numpy.array(xTrain).reshape(-1, 1), residuals)
    ##使用最新的模型预测数据
    latestInSamplePrediction = modelList[-1].predict(numpy.array(xTrain).reshape(-1, 1))
    ##更新残差
    residuals = [residuals[i] - eps * latestInSamplePrediction[i] for i in range(len(residuals))]
    ##在测试集上使用模型
    latestOutSamplePrediction = modelList[-1].predict(numpy.array(xTest).reshape(-1, 1))
    ##加入预测值列表
    predList.append(list(latestOutSamplePrediction))


##均方差列表
mse = []
##在测试集上的预测值之和的列表
allPredictions = []
i=0
##通过误差累计的方式筛选列表
for iModels in range(len(modelList)):
    prediction = []
    ##此循环的目的：每个模型都是把前面的所有的模型的预测值加起来，形成一个新列表
    for iPred in range(len(xTest)):
        prediction.append(sum([predList[i][iPred] for i in range(iModels + 1)]) * eps)
    ##添加到列表
    allPredictions.append(prediction)
    ##计算新的离差
    errors = [(yTest[i] - prediction[i]) for i in range(len(yTest))]
    ##均方差：即离差的平方和的平均数
    mse.append(sum([e * e for e in errors]) / len(yTest))

'''
   第五步：绘图观察结果
'''
##模型个个数+1，绘图用：即模型列表中的从0开始的下标变成从1开始 的编号
nModels = [i + 1 for i in range(len(modelList))]

##绘制均方差和模型个数变化曲线
plot.plot(nModels,mse)
plot.axis('tight')
plot.xlabel('Number of Models in Ensemble')
plot.ylabel('Mean Squared Error')
plot.ylim((0.0, max(mse)))
plot.show()

##绘制模型曲线和真实值曲线的对比
plotList = [0, 14, 29]
lineType = [':', '-.', '--']
plot.figure()
for i in range(len(plotList)):
    iPlot = plotList[i]
    textLegend = 'Prediction with ' + str(iPlot) + ' Trees'
    plot.plot(xTest, allPredictions[iPlot], label = textLegend, linestyle = lineType[i])
plot.plot(xTest, yTest, label='True y Value', alpha=0.25)
plot.legend(bbox_to_anchor=(1,0.3))
plot.axis('tight')
plot.xlabel('x value')
plot.ylabel('Predictions')
plot.show()

