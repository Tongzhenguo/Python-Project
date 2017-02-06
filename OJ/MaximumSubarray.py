# coding=utf-8
__author__ = 'arachis'

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
找到最大子数组和
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0 for i in nums]##dp[i] means the maximum subarray ending with A[i];
        dp[0] = nums[0]
        maxSum = dp[0]

        for i in range(1,n,1):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0) #状态转移方程（递推式）
            print dp[i]
            maxSum = max(maxSum, dp[i])
        return maxSum
print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])