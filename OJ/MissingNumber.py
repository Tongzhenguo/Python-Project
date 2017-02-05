# coding=utf-8
__author__ = 'arachis'

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
给定n个不同元素组成的整型数组nums，这些元素是0 to n （n+1个数）的序列，找到没有出现的那个数
For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
要求：线性时间复杂度，最好使用较少的内存空间
"""

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        list = range(0, n + 1)
        return (set(list) - set(nums)).pop()

    def topSolution(self, nums):
        """
        The basic idea is to use XOR operation.
        We all know that a^b^b =a, which means two xor operations with the same number will eliminate the number and reveal the original number.
        In this solution, I apply XOR operation to both the index and value of the array.
        In a complete array with no missing numbers, the index and value should be perfectly corresponding( nums[index] = index),
        so in a missing array, what left finally is the missing number.

        """
        xor,n = 0,len(nums)
        for i in range(len(nums)):
            xor = xor ^ i ^ nums[i]
        return xor ^ n

print Solution().topSolution([0, 1, 3])
# print Solution().topSolution([0])