# coding=utf-8
## GUI使得人们可以在预剪枝时测试不同参数的影响，还可以帮助我们选择模型的类型
##利用现有模块Tkinter来构建GUI
from Tkinter import *

from numpy import mat, arange

from MachineLearningInAction.decisonTree.regressionTree import regTrees
from MachineLearningInAction.decisonTree.regressionTree.regTrees import modelLeaf, modelErr, createForeCast, \
    modelTreeEval, createTree

"""
Matplotlib和Tkinter的代码集成
"""
import matplotlib

matplotlib.use("TkAgg")  ###设定后端是TkAgg


def reDraw(tolS, tolN):
    """绘制一棵树
    :param tolS:
    :param tolN:
    :return:
    """
    reDraw.f.clf()
    reDraw.a = reDraw.f.add_subplot(111)
    if (chkBtnVar.get()):  ##检查复选框是否选中
        if (tolN < 2):
            tolN = 2
        myTree = regTrees.createTree(reDraw.rawDat, modelLeaf, modelErr, (tolS, tolN))
        yHat = createForeCast(myTree, reDraw.testDat, modelTreeEval)
    else:
        myTree = createTree(reDraw.rawDat, (tolS, tolN))
        yHat = createForeCast(myTree, reDraw.testDat)
    ##绘制离散真实值
    reDraw.a.scatter(reDraw.rawDat[:, 0], reDraw.rawDat[:, 1], s=5)
    ##绘制连续预测值
    reDraw.a.plot(reDraw.testDat, yHat, linewidth=2.0)
    reDraw.canvas.show()


def getInputs():
    """从文本框中获取特征数和样本数
    :return:
    """
    try:
        tolN = int(tolNentry.get())
    except:
        tolN = 10
        print "enter Integer for tolN"
        tolNentry.delete(0, END)
        tolNentry.insert(0, '10')
    try:
        tolS = int(tolSentry.get())
    except:
        tolS = 1.0
        print "enter Integer for tolS"
        tolSentry.delete(0, END)
        tolSentry.insert(0, '1.0')
    return tolN, tolS


def deawNewTree():
    """根据输入的tolN和tolS画一颗树
    :return:
    """
    tolN, tolS = getInputs()
    reDraw(tolN, tolS)


"""
用于构建树管理器界面的Tkinter小部件
"""
root = Tk()
Label(root, text="Plot Place Holder").grid(row=0, columnspan=3)
Label(root, text="tolN").grid(row=1, column=0)
tolNentry = Entry(root)
tolNentry.grid(row=1, column=1)
tolNentry.insert(0, '10')
Label(root, text='tolS').grid(row=2, column=0)
tolSentry = Entry(root)
tolSentry.grid(row=2, column=1)
tolSentry.insert(0, '1.0')
Button(root, text="ReDraw", command=deawNewTree).grid(row=1, column=2, rowspan=3)

chkBtnVar = IntVar()
chkBtn = Checkbutton(root, text="Model Tree", variable=chkBtnVar)
chkBtn.grid(row=3, column=0, columnspan=2)

reDraw.rawDat = mat(regTrees.loadDataSet('F:\code\Python-Project\dataset\sine.txt'))
reDraw.testDat = arange(min(reDraw.rawDat[:, 0]), max(reDraw.rawDat[:, 0]), 0.01)
reDraw(1.0, 10)
root.mainloop()
