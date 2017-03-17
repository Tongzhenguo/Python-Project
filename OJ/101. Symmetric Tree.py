# coding=utf-8
__author__ = 'arachis'
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
判断一个二叉树是不是中心对称的，可分别设计迭代算法和递归算法
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

class Solution(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isSymmetricHelp(root.left, root.right)

    def isSymmetricHelp(self,left, right):
        if(left==None or right == None): #两边都是空
            return left==right
        if(left.val != right.val):
            return False #轴对称，左左右右，左右右左
        return self.isSymmetricHelp(left.left, right.right) and self.isSymmetricHelp(left.right, right.left)