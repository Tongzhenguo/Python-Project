# coding=utf-8
__author__ = 'arachis'
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
输入是一个二叉树和一个整数，判断是否存在一条从根到叶结点的路径，所有元素加起来的和等于输入的整数
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

class Solution(object):
    """
    一个维护当前节点的前缀路由的和，列表存储各路径和，直到叶结点判断是否相等
    遍历返回的列表，判断是否有相等的
    """
    def trival(self,root,path,sumList):
        if root == None: return sumList #当前空节点
        if root.left == None and root.right == None: #叶结点，添加路径和
            sumList.append( path+root.val )
        if root.right == None: #右分支不存在叶结点
            self.trival( root.left,path+root.val,sumList )
        if root.left == None: #左分支不存在叶结点
            self.trival( root.right,path+root.val,sumList )
        else: #左右都存在
            self.trival( root.left,path+root.val,sumList )
            self.trival( root.right,path+root.val,sumList )
        return sumList

    def hasPathSum(self, root, sum):
        if root == None: return False
        sumList = self.trival(root, 0, [])
        for i in sumList:
            if i == sum : return True
        return False