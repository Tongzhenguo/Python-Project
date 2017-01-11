# coding=utf-8

__author__ = 'arachis'

"""
Given an array of integers and an integer k,
 find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

简单翻译就是判断一个整型数组任意截取长度为k的片段内是否有重复
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        minDist = float("inf")
        idx = {}
        for i in xrange(len(nums)):
            if(idx.has_key(nums[i]) and i - idx[nums[i]] < minDist ):
                minDist = i - idx[nums[i]]
            idx[nums[i]] = i
        return minDist <= k

# print Solution().containsNearbyDuplicate([1,2,3,4,5,6,1,4,5,67,76]*100,10)