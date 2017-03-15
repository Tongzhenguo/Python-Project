# coding=utf-8
import collections

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
优化：是否可以只适用递归，不使用额外空间的情况下解决此问题
"""

# class Solution(object):
#     def dfs(self,node,count):
#         if node:
#             count[node.val] += 1
#             self.dfs(node.left,count)
#             self.dfs(node.right,count)
#
#     def findMode(self, root):#O(n)空间
#         count = collections.Counter()
#         self.dfs(root,count) #记录所有
#         return [k for k, v in count.iteritems() if v == max(count.itervalues())]
#超时

