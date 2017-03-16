# coding=utf-8
__author__ = 'arachis'
"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
判断是否是平衡二叉树，即两个子树的高度差不超过1
"""

class Solution(object):
    """
    返回当前节点的高度
    """
    def depth(self,root):
        if root == None:
            return 0
        return 1 + max( self.depth( root.left ) , self.depth( root.right ) )
    def isBalanced(self, root):
        if root == None:
            return True
        if abs( self.depth( root.left ) - self.depth( root.right ) ) > 1 :
            return False
        else:
            return self.isBalanced( root.left ) and self.isBalanced( root.right )