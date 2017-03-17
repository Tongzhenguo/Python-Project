# coding=utf-8
__author__ = 'arachis'
"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
对于二叉查找树，每个元素值都是非负数，找到任意两个节点差的最小值
Example:
Input:
   1
    \
     3
    /
   2
Output:
1
Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""

class Solution(object):
    """
    The most common idea is to first inOrder traverse the tree and compare the delta between each of the adjacent values.
    It's guaranteed to have the correct answer because it is a BST thus inOrder traversal values are sorted.
    Solution 1 - In-Order traverse, time complexity O(N), space complexity O(1).
    """
    def __init__(self):
        self.cur = 2 ** 32 - 1 #当前最小值
        self.pre = None #将每次遍历到的值都存到栈里
    def getMinimumDifference(self, root):
        if root == None: return self.cur
        self.getMinimumDifference(root.left) #找到左子树中最小差
        if (self.pre != None and abs(root.val - self.pre) < self.cur ) :
            self.cur = abs(root.val - self.pre)
        self.pre = root.val
        self.getMinimumDifference(root.right)
        return self.cur