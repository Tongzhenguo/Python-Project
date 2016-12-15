# coding=utf-8
from numpy import *


def loadDataset(fileName):
	dataMat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float, curLine)
		dataMat.append(fltLine)
	return dataMat

def distEclud(vecA, vecB):
	""" 计算两个向量的欧式距离
	:param vecA:
	:param vecB:
	:return:
	"""
	return sqrt(sum(power(vecA-vecB, 2)))
	
def randCent(dataMat, k):
	""" 随机初始化k个类簇的中心
	:param dataMat:
	:param k:
	:return:
	"""
	n = shape(dataMat)[1]
	centroids = mat(zeros((k,n)))
	for j in range(n):
		minJ = min(dataMat[:,j])
		rangeJ = float(max(dataMat[:,j]) - minJ)
		centroids[:,j] = minJ + rangeJ * random.rand(k,1)
	return centroids

def kMeans(dataSet, k, distMeas = distEclud, createCent = randCent):
	"""kmeans 算法
	:param dataSet:
	:param k: 类簇的个数
	:param distMeas: 计算相似距离的函数
	:param createCent: 指定初始类簇的函数
	:return:类簇矩阵和样本分配簇矩阵
	簇分配结果矩阵包括两列：簇索引值和误差（当前点到簇中心的距离）
	"""
	m = shape(dataSet)[0]
	clusterAssment = mat(zeros((m,2)))
	centroids = createCent(dataSet, k)
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		for i in range(m):
			minDist = inf; minIndex = -1
			for j in range(k):
				distJI = distMeas(centroids[j,:], dataSet[i,:])
				if distJI < minDist:
					minDist = distJI; minIndex = j
			if clusterAssment[i,0] != minIndex: clusterChanged = True
			clusterAssment[i,:] = minIndex, minDist**2
		# print centroids
		for cent in range(k):
			ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]
			centroids[cent,:] = mean(ptsInClust, axis=0)
	return centroids, clusterAssment

## test
# datMat = mat(loadDataset('testSet.txt'))
# myCentroids, clustAssing = kMeans(datMat, 4)

def biKmeans(dataSet, k, distMeas=distEclud):
	""" 二分k均值算法
	该算法初始聚类为一个簇，之后迭代二分均值，选择SSE最大的簇再二分
	:param dataSet:
	:param k:
	:param distMeas:
	:return:
	"""
	m = shape(dataSet)[0]
	clusterAssment = mat(zeros((m,2)))
	centroid0 = mean(dataSet, axis = 0).tolist()[0]
	centList = [centroid0]#初始簇
	for j in range(m):
		clusterAssment[j,1] = distMeas(mat(centroid0), dataSet[j,:])**2
	while (len(centList) < k):
		lowestSSE = inf
		for i in range(len(centList)):## 遍历所有的簇以决定最佳的簇进行划分
			ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]
			centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
			sseSplit = sum(splitClustAss[:,1])
			sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
			print "sseSplit, and notSplit: ", sseSplit, sseNotSplit
			## 新二分的簇的误差和与其余簇误差作为本次划分误差,如果本次误差最小，则本次误差被保存
			if (sseSplit + sseNotSplit) < lowestSSE:
				bestCentToSplit = i
				bestNewCents = centroidMat
				bestClustAss = splitClustAss.copy()
				lowestSSE = sseSplit + sseNotSplit ##更新簇的分配结果
		bestClustAss[nonzero(bestClustAss[:,0].A==1)[0], 0] = len(centList)
		bestClustAss[nonzero(bestClustAss[:,0].A==0)[0], 0] = bestCentToSplit
		print "The bestCentToSplit is: ", bestCentToSplit
		print "The len of bestClustAss is: ", len(bestClustAss)
		centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]
		centList.append(bestNewCents[1,:].tolist()[0])
		clusterAssment[nonzero(clusterAssment[:,0].A==bestCentToSplit)[0],:] = bestClustAss
	return mat(centList), clusterAssment

#this is a test
# datMat3 = mat(loadDataset('testSet2.txt'))
# centList, myNewAssments = biKmeans(datMat3,3)

def distSLC(vecA, vecB):
	""" 计算球面余弦距离
	:param vecA:
	:param vecB:
	:return:
	"""
	a = sin(vecA[0,1]*pi/180) * sin(vecB[0,1]*pi/180)
	b = cos(vecA[0,1]*pi/180) * cos(vecB[0,1]*pi/180) *\
	 cos(pi*(vecB[0,0]-vecA[0,0])/180)
	return arccos(a+b)*6371.0


import matplotlib.pyplot as plt
def clusterClubs(numClust=5):
	datList = []
	for line in open('places.txt').readlines():
		lineArr = line.split('\t')
		datList.append([float(lineArr[4]), float(lineArr[3])])
	datMat = mat(datList)
	myCentroids, clustAssing = biKmeans(datMat, numClust, distMeas = distSLC)
	fig = plt.figure()
	rect = [0.1, 0.1, 0.8, 0.8]
	scatterMarkers = ['s', 'o', '^', '8', 'p', 'd', 'v', 'h', '>', '<']
	axprops = dict(xticks=[], yticks=[])
	ax0 = fig.add_axes(rect, label = 'ax0', **axprops)
	imgP = plt.imread('Portland.png')
	ax0.imshow(imgP)
	ax1 = fig.add_axes(rect, label = 'ax1', frameon = False)
	for i in range(numClust):
		ptsInCurrCluster = datMat[nonzero(clustAssing[:,0].A == i)[0],:]
		markerSytle = scatterMarkers[i%len(scatterMarkers)]
		ax1.scatter(ptsInCurrCluster[:,0].flatten().A[0], \
			ptsInCurrCluster[:,1].flatten().A[0],\
			marker = markerSytle, s=90)
	ax1.scatter(myCentroids[:,0].flatten().A[0], myCentroids[:,1].flatten().A[0],\
		marker = '+', s=300)
	plt.show()
clusterClubs(6)