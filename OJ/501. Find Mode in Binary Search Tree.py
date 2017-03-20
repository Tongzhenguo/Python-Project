# coding=utf-8
__author__ = 'arachis'
"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
输入是一个二叉排序树（BST）,元素有重复，找到重复出现次数最多的元素，返回这些元素的列表
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
优化：是否可以只用递归，不使用额外空间的情况下解决此问题
"""

class Solution(object):  ##BST优化的方法
    def __init__(self):
        #记录当前最大频次
        self.cur = 0
        #保存最大频次对应的元素
        self.modes = [0]
        #modes中的元素个数
        self.modeCount = 0
        #现在正访问的值
        self.currVal = 0
        #现在正访问的值出现的频次
        self.currValCount = 0
    def inorder(self,root):
        #有重复BST性质：left <= root <= right,有序遍历中找到相等的元素
        if root:
            self.inorder(root.left)

            if( root.val != self.currVal ):
                self.currValCount = root.val
                self.currValCount = 0
            self.currValCount += 1

            if( self.currValCount > self.cur ):
                self.cur = self.currValCount
                self.modeCount = 1

            if( self.currValCount == self.cur ):
                if (self.modes != None):
                    self.modes[self.modeCount-1] = self.currVal #越界
                self.modeCount += 1

            self.inorder(root.right)

    def findMode(self, root):#O(n)空间
        self.inorder(root)
        return self.modes


# class Solution(object):  ##BST和普通二叉树同样适用
#     def __init__(self):
#         self.cur = 0
#     def dfs(self,node,count):
#         if node:
#             count[node.val] = 1+count.get(node.val,0)
#             if count[node.val] > self.cur: self.cur = count[node.val]
#             self.dfs(node.left,count)
#             self.dfs(node.right,count)
#
#     def findMode(self, root):#O(n)空间
#         count = {}
#         self.dfs(root,count) #记录所有
#         return [k for k, v in count.iteritems() if v == self.cur ]




