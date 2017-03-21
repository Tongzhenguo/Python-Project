# coding=utf-8
__author__ = 'arachis'

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
给定一个M*N的矩阵，求从左上角到右下角的所走过的路径的和的最小值，注：只能下移和右移
Note: You can only move either down or right at any point in time.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        DP问题练习：
        初值：dp[0][0] = grid[0][0];dp[0][j]=dp[0][j-1]+grid[0][j];dp[i][0]=dp[i-1][0]+grid[i][0]
        递推式：dp[i][j] = min(dp[i][j-1]+grid[i][j],dp[i-1][j]+grid[i][j])
        O(N2),O(N)
        """
        dp = grid
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if(i==0):
                    if(j==0):
                        dp[0][0] = grid[0][0]
                    else:
                       dp[0][j]=dp[0][j-1]+grid[0][j]
                elif(j==0):
                    dp[i][0]=dp[i-1][0]+grid[i][0]
                else:
                   dp[i][j] = grid[i][j] +min(dp[i][j-1],dp[i-1][j])
        return dp[i][j]

# print Solution().minPathSum([[1,1,100],[2,2,100],[1,1,1]])