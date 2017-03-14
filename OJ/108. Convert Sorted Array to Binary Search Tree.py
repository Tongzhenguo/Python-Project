# coding=utf-8
from datastructure.TreeNode import TreeNode

__author__ = 'arachis'
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
给定升序的数组，将这个数组转成高度平衡的二叉排序树
"""

class Solution(object):
    def helper(self , num, low,  high):
        #二分法
        if (low > high):
            return None
        mid = (low + high) / 2
        root = TreeNode(num[mid])
        root.left = self.helper(num, low, mid - 1)
        root.right = self.helper(num, mid + 1, high)
        return root
    def sortedArrayToBST(self, nums):
        if ( len(nums) == 0) : return None
        root = self.helper(nums, 0,len(nums) - 1)
        return root