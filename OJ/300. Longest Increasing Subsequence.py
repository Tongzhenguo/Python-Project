# coding=utf-8
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
对于一个无序的整型数组，找到递增数列的最大长度
For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.
要求：时间复杂度应该是O(n2)，最好O(n log n)
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution(object):
        def lengthOfLIS(self, nums):
            """
            DP练习：
            dp[i]:所有长度为i+1的LIS中坐标i对应的最小值
             """
            tails = [0] * len(nums)
            size = 0
            for x in nums:
                i, j = 0, size
                while i != j:
                    m = (i + j) / 2
                    if tails[m] < x:
                        i = m + 1
                    else:
                        j = m
                tails[i] = x
                size = max(i + 1, size)
            return size
# print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])