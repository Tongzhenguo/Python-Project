# coding=utf-8
from numpy import *


def createDataSet():
	group = array([
		[1.0,1.1],
		[1.0,1.0],
		[0,0],
		[0,0.1]
	])
	labels = ["A","A","B","B"]
	return group,labels

def classify0(inX,dataSet,labels,k):
	"""
	:param inX:待分类的向量
	:param dataSet: 训练数据集
	:param labels: 标签向量
	:param k: 最近个数
	:return:
	注：tile 是将inX重复detaSetSize次来构造一个新矩阵
	"""
	detaSetSize = dataSet.shape[0] ##距离计算
	diffMat = tile(inX,(detaSetSize,1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort() #返回排序之后的索引ndarray
	classCount={}
	for i in range(k): ##计数
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.items(),key=lambda p:p[1],reverse=True)
	return sortedClassCount[0][0] ##返回多数表决结果

## this is a test for classify0
group,labels = createDataSet()
# print classify0([0,0],group,labels,3)

def file2matrix(filename):
	fr = open(filename)
	arrayLines = fr.readlines()
	numberOfLines = len(arrayLines)
	returnMat = zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector


datingDataMat,datingLabels = file2matrix("F:\code\Python-Project\dataset\datingTestSet2.txt")

# import matplotlib
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ## 后两个参数控制色彩和尺寸
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()

def autoNorm(dataSet):
	""" 对样本进行最大最小归一化，以防止因为某维特征值过大使得距离计算失效
	:param dataSet:
	:return: normDataSet,ranges,minVals
	"""
	minVals = dataSet.min(0) ##计算每一列的最小值
	maxVals = dataSet.max(0) ##计算每一列的最大值
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0] ##矩阵的减法
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet / tile(ranges,(m,1))
	return normDataSet,ranges,minVals

## this is a test for autoNorm
normMat,ranges,minVals = autoNorm(datingDataMat)
# print normMat

def datingClassTest():
	hoRatio = 0.10
	datingDataMat, datingLabels = file2matrix('F:\code\Python-Project\dataset\datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio) ##分割训练集，测试集
	errorCount = 0.0
	for i in range(numTestVecs): ## 计算错误率（0-1损失函数）
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],\
				datingLabels[numTestVecs:m],3)
		print "the classifier came back with: %d, the real answer is: %d"\
				% (classifierResult, datingLabels[i])
		if(classifierResult != datingLabels[i]): errorCount += 1.0
	print "the total error rate is: %f" % (errorCount/float(numTestVecs))

## this is a test for datingClassTest()
# datingClassTest()

def classifyPerson():
	""" knn预测是约会喜欢程度
	:return:
	"""
	resultList = ['not at all','in small doses','in large doses']
	percentTats = float(raw_input(\
				"percentage of time spent playing video games>"))
	ffMiles = float(raw_input("frequent flier miles earned per year?"))
	iceCream = float(raw_input("liters of ice cream consumed per year?"))
	datingDataMat, datingLabels = file2matrix('F:\code\Python-Project\dataset\datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles, percentTats, iceCream])
	classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
	print "You will probably like this person: ", resultList[classifierResult - 1]

## this is a test
# classifyPerson()

def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect

# test
# vector = img2vector("F:/code/Python-Project/dataset/testDigits/0_13.txt")
# print vector

from os import listdir
def handwritingClassTest():
	hwLabels = []
	train_path = 'F:/code/Python-Project/dataset/trainingDigits'
	test_path = 'F:/code/Python-Project/dataset/testDigits'
	trainingFileList = listdir(train_path)
	m = len(trainingFileList)
	trainingMat = zeros((m,1024))
	for i in range(m):## 解析训练集文件
		flleNameStr = trainingFileList[i]
		fileStr = flleNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector(train_path+'/%s' % flleNameStr)

	testFileList = listdir(test_path)
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector(test_path+'/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
		print "the classifier came back with: %d, the real answer is: %d" \
				% (classifierResult, classNumStr)
		if(classifierResult != classNumStr): errorCount += 1.0
	print "\nthe total number of errors is: %d" % errorCount
	print "\nthe total error rate is: %f" % (errorCount/float(mTest))

## 测试手写识别的例子
handwritingClassTest()











