# coding=utf-8
"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.
给定非负数组和一个S,将S用数组中所有元素的线性加权表示出来，系数只能是+1，-1，请问有多少种表示法？
注：数组长度0<n<=20,sum(nums[:n+1])<=1000,返回值是int32
Find out how many ways to assign symbols to make sum of integers equal to target S.

"""


def subsetSum(nums, s):
    """
    DP练习：
    Find a subset P of nums such that sum(P) = (target + sum(nums)) / 2
    dp[i]:P中包含有nums[i]的个数
    dp[0]=1
    dp[j]=dp[j-num];j>0
    """
    dp = [0] * (s+1)
    dp[0] = 1
    for num in nums:
        for j in range(s , num-1, -1):
            dp[j] += dp[j - num]
    return dp[s]

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        Let P be the positive subset and N be the negative subset，=>
                          sum(P) - sum(N) = target
        sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)
        So the original problem has been converted to a subset sum problem as follows:
        Find a subset P of nums such that sum(P) = (target + sum(nums)) / 2
        """
        sumn = sum(nums)
        if (S > sumn or (sumn + S) % 2 == 1): return 0
        else:
            return subsetSum(nums, (S+sumn)/2)
print Solution().findTargetSumWays([1, 1, 1, 1, 1],3)