# coding=utf-8
__author__ = 'arachis'

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
找到指定数组中出现floor(n/3),n是数组长度，的数；要求时间是0(n),空间是常数的
"""

class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        # since the requirement is finding the majority for more than ceiling of [n/3], the answer would be less than or equal to two numbers.
        #So we can modify the algorithm to maintain two counters for two majorities.
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) / 3]