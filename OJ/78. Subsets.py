# coding=utf-8
__author__ = 'arachis'
"""
Given a set of distinct integers, nums, return all possible subsets.
给定去重的集合，设计算法找到所有可能的子集集合
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        """
        res = []
        res.append([])
        m = len(nums)
        for i in range(m+1):
            for j in range(i+1,m+1):
                res.append( nums[i:j] )
        return res
print Solution().subsets([1,2,3])