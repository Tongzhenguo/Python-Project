# coding=utf-8
__author__ = 'arachis'
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.
给定整数集合，返回所有可能的子集，子集不能重复
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution:
    """先排序，如果遇到相同的就把他加入到前
    if S[i] is same to S[i - 1], then it needn't to be added to all of the subset,
    just add it to the last l subsets which are created by adding S[i - 1]
    """
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                # print res
                res.append(res[j] + [S[i]])
        return res
print( Solution().subsetsWithDup([1,2,2]) )