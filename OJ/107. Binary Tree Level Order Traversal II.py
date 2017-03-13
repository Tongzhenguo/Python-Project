# coding=utf-8
__author__ = 'arachis'
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
遍历一棵树，返回一个列表，以从底向上的顺序存储列表，每一层按从左到右的顺序，如[
  [15,7],
  [9,20],
  [3]
]是二叉树
    3
   / \
  9  20
    /  \
   15   7
的返回结果
"""

class Solution(object):
    """
    维护一个全局列表，存储每层元素
    维护一个变量，标识当前层数
    """
    def levelOrderBottom(self, root):
        if root == None: return []
        wrapList = [[]]
        self.levelMaker(wrapList, root, 0)
        return wrapList
    def levelMaker(self,list,root,level):
        if(root == None): return
        if(level >= len(list) ) : list.insert(0,[]) #bottom to up
        self.levelMaker(list, root.left, level+1) #update left subtree
        self.levelMaker(list, root.right, level+1) #update right subtree
        list[ len(list)-1-level ].append(root.val) #set list