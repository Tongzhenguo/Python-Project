# coding=utf-8
## FP树的类定义
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        """初始化树节点
        :param nameValue: 元素名字
        :param numOccur: 元素出现次数
        :param parentNode: 父节点
        """
        self.name = nameValue
        self.count = numOccur  ##计数值
        self.nodeLink = None  ##用于链接相似的元素项
        self.parent = parentNode  ##指向父节点的指针
        self.children = {}  ##存放节点的子节点

    def inc(self, numOccur):
        """debug用
        :param numOccur:
        :return:
        """
        self.count += numOccur

    def disp(self, ind=1):
        """debug用
        :param ind:缩进控制（" " * ind）
        :return:
        """
        print " " * ind, self.name, " ", self.count
        for child in self.children.values():
            child.disp(ind + 1)


# rootNode = treeNode('pyramid',9,None)
# rootNode.children['eye']=treeNode("eye",13,None)
# rootNode.children['phoenix']=treeNode("phoenix",3,None)
# print rootNode.disp()

##FP树构建函数
def updateHeader(nodeToTest, targetNode):
    """更新头节点字典
    :param nodeToTest:节点
    :param targetNode: 目标节点
    :return:空
    """
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode


def updateTree(items, inTree, headerTable, count):
    """更新树
    :param items:排序后的元素
    :param inTree: FP树
    :param headerTable: 头节点字典
    :param count: 计数值
    :return:空
    """
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if (headerTable[items[0]][1] == None):
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if (len(items) > 1):  ##对剩下的元素项迭代调用updateTree
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)


def createTree(dataSet, minSup=1):
    """FP树构建函数
    树构建过程中会遍历数据集两次
    第一次遍历统计每个元素项出现的频度
    第二次只遍历频繁项
    :param dataSet: 数据集
    :param minSup: 最小支持度
    :return:FP树和头节点字典
    """
    headerTable = {}  ##头节点字典
    for trans in dataSet:  ##第一次遍历统计每个元素项出现的频度
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in headerTable.keys():  ##移除头指针字典中不满足最小支持度的元素项
        if (headerTable[k] < minSup):
            del (headerTable[k])
    freqItemSet = set(headerTable.keys())
    if (len(freqItemSet) == 0):
        return None, None  ##如果没有元素项满足要求则退出
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    retTree = treeNode("Null Set", 1, None)
    for tranSet, count in dataSet.items():  ##第二次只遍历频繁项集
        localD = {}
        for item in tranSet:
            if (item in freqItemSet):
                localD[item] = headerTable[item][0]
        if (len(localD) > 0):  ##根据全局概率对每个事务中的元素进行排序
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)  ##使用排序后的频率项集对树进行填充
    return retTree, headerTable


##简单数据集及数据包装器
def loadSimpleDat():
    simpDat = [
        ["r", "z", "h", "j", "p"],
        ["z", "y", "x", "w", "v", "u", "t", "s"],
        ["z"],
        ["r", "x", "n", "o", "s"],
        ["y", "r", "x", "z", "q", "t", "p"],
        ["y", "z", "x", "e", "q", "s", "t", "m"]
    ]
    return simpDat


def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict


# simpleDat = loadSimpleDat()
# print simpleDat
# initSet = createInitSet(simpleDat)
# myFPtree,myHeaderTab = createTree(initSet, 3)
# myFPtree.disp()

##发现以给定元素项结尾的所有路径的函数
def ascendTree(leafNode, prefixPath):
    """迭代上溯整棵树
    :param leafNode:给定要查找的叶子节点
    :param prefixPath: 前缀路径(从上到下经过的路径)
    :return:
    """
    if (leafNode.parent != None):  # 迭代上溯整棵树
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(basePat, treeNode):
    """
    :param basePat:要查找
    :param treeNode:查找的树节点
    :return:条件模式基
    """
    condPats = {}  ##条件模式基
    while (treeNode != None):
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if (len(prefixPath) > 1):
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

# simpleDat = loadSimpleDat()
# initSet = createInitSet(simpleDat)
# myFPtree,myHeaderTab = createTree(initSet, 3)
# print findPrefixPath("x",myHeaderTab["x"][1])
# print findPrefixPath("r",myHeaderTab["r"][1])
