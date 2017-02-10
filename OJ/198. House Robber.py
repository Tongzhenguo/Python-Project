# coding=utf-8
__author__ = 'arachis'

"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
你是一个专业的强盗计划抢一条街的房子。每个房子都有一定金额的钱，但是相邻的房子有安全系统连接，
给一个表示每个房子的钱数的非负整数列表，确定你今晚可以抢夺的最大金额，而不警告警察。
"""

class Solution(object):
    def rob(self, nums):
        """
        DP问题练习：
        dp[i]表示第i房子抢到的最大金额
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        dp[i>2] = max(dp[i-1],dp[i-2]+nums[i])
        """
        dp,n = nums,len(nums)
        if n==0 :return 0
        if n==1:return nums[0]
        dp[1] = max(nums[0],nums[1])
        maxP = dp[1]
        for i in range(2,n,1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            if(maxP<dp[i]):maxP = dp[i]
        return maxP
# print Solution().rob([])
# print Solution().rob([1])
# print Solution().rob([2,1])
# print Solution().rob([1,3,1,3,100])