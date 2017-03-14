# coding=utf-8
__author__ = 'arachis'
"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
树的最小深度是从根节点到最近的叶子节点的最短路径长度，求二叉树的最小深度
"""
class Solution(object):
    def minDepth(self, root):
        """
        遍历树，选择左右子树中最小的深度
        """
        if root == None : return 0
        if root.left != None and  root.right == None: #只有左分支，深度由左分支决定
            return 1+self.minDepth( root.left )
        if root.right != None and root.left == None:# 只有右分支，深度由左分支决定
            return 1+self.minDepth( root.right )
        return min( 1+self.minDepth(root.left) , 1+self.minDepth(root.right) ) #选择最小的子树