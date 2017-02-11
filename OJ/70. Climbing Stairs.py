# coding=utf-8
__author__ = 'arachis'

"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
加入你爬一个n阶的楼梯，每次只能一到两阶，问有多少种路线
Note: Given n will be a positive integer.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        DP问题练习
        dp[i]是爬i阶的路线数
        dp[0]=0
        dp[1]=1
        dp[i]=dp[i-1]+dp[i-2]
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if(n>2):
            dp = []
            dp.append(0)
            dp.append(1)
            dp.append(2)
            for i in range(3,n+1,1):
                dp.append(dp[i-1]+dp[i-2])
            return dp[n]

# print Solution().climbStairs(3)
