# coding=utf-8
__author__ = 'arachis'

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
Note:m and n will be at most 100.
给一个m*n(<100*100)的网格，从左上角到右下角移动，约定只能右移或下移，问有多少种轨迹？
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        DP问题练习：
        这里的dp[i][j]代表通过(i,j)坐标
        dp[0][0]=1,dp[i][0]=dp[i-1][0],dp[0][j]=dp[0][j-1]
        dp[i][j] = dp[i-1][j]+ dp[i][j-1]
        """
        dp = []
        for i in range(m):
            dp.append([0 for k in range(n)])
            for j in range(n):
                if(i==0):
                    if(j==0):
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j-1]
                elif(j==0):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
# print Solution().uniquePaths(3,2)