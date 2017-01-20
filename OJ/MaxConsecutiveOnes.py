# coding=utf-8
import time

__author__ = 'arachis'

"""
    Given a binary array, find the maximum number of consecutive 1s in this array.
    简单翻译就是求二进制数组的最长连续1的序列的个数
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxC ,counter = 0,0
        for i in nums:
            if(i == 1):
                counter += 1
            else:
                if(counter > maxC): #update maxC only when i == 0 ,to reduce the nums of operation
                    maxC = counter
                counter = 0
        return counter if counter > maxC else maxC ## when final element is 0