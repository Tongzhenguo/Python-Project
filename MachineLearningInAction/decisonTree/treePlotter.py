# coding=utf-8
###plot :绘制
import matplotlib.pyplot as plt
##定义文本框和箭头格式
desicionNode = dict(boxstyle='sawtooth',fc='0.8')
leafNode = dict(boxstyle='round4',fc='0.8')
arrow_args = dict(arrowstyle='<-')
def createPlot():
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    ##绘图区
    createPlot.ax1 = plt.subplot(111,frameon=False)
    plotNode('a decision node',(0.5,0.1),(0.1,0.5),desicionNode)
    plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    """绘制箭头注解（annotate）
    :param nodeTxt:
    :param centerPt:
    :param parentPt:
    :param nodeType:
    :return:
    """
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,
                            xycoords='axes fraction',
                            xytext=centerPt,textcoords='axes fraction',
                            va='center',ha='center',bbox=nodeType,
                            arrowprops=arrow_args)
# print createPlot()
## 绘制一棵树需要知道树的宽和高，也即叶结点数和数的深度
def getNumLeafs(myTree):
    """获得数的叶子数
    :param myTree:数的字典表示
    :return:叶子数
    """
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__ == 'dict'):
            numLeafs +=getNumLeafs(secondDict[key])
        else:
            numLeafs +=1
    return numLeafs
def getTreeDepth(myTree):
    """获取数的深度
    :param myTree:以字典表示的树
    :return: 深度
    """
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict:
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1+ getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth
def retrieveTree(i):
    listOfTrees =[
        {'no surfacing':{0: 'no', 1: { 'flippers':{0:'no', 1:'yes'}}}},
        {'no surfacing':{0: 'no', 1: { 'flippers':{0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
    ]
    return listOfTrees[i]
def plotMidText(cntrPt,parentPt,txtString):
    """在父子节点间填充文本信息
    :param cntrPt: 子节点坐标
    :param parentPt:父节点坐标
    :param txtString: 节点间文本
    :return:
    """
    xMid = (parentPt[0]-cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)
def plotTree(myTree,parentPt,nodeText):
    """
    :param myTree:
    :param parentPt:
    :param nodeText:
    :return:
    """
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    ##计算节点中心坐标
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff)
    ##标记子节点属性值
    plotMidText(cntrPt,parentPt,nodeText)
    plotNode(firstStr,cntrPt,parentPt,desicionNode)
    secondDict = myTree[firstStr]
    ##递减y坐标值
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__ == 'dict'):
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,desicionNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    ## 下一层的y坐标
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
def createPlot(inTree):
    """ 绘图主函数，调用了plotTree
    :param inTree:
    :return:
    """
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    createPlot.ax1 = plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    ##两个全局变量计算和跟踪节点绘制位置
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree,(0.5,1.0),'')
    plt.show()
#myTree = retrieveTree(0)
#print createPlot(myTree)
# print getNumLeafs(myTree)
# print getTreeDepth(myTree)
