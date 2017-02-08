# coding=utf-8
__author__ = 'arachis'

"""
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
obstacles:障碍
与Unique Paths问题相同，给定m*n（<100*100）的网格，对于给定位置nums[i][j]存在障碍,则为1；否则为0
要求每次只能下移和右移,求可通过的路径数
例如：
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
返回结果为2

"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        DP问题练习：
        这里的dp[i][j]代表通过(i,j)坐标有多少种路径
        初值：
        dp[0][0]=0 if obstacleGrid[0][0] == 1 else 1
        dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
        dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
        递推公式：
        dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i-1][j]+ dp[i][j-1]
        """
        dp = obstacleGrid
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if(i==0):
                    if(j==0):
                        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1 ##当前是阻碍，0种路径
                    else:
                        dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
                elif(j==0):
                    dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
                else:
                    dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i-1][j]+ dp[i][j-1]
        return dp[m-1][n-1]
# print Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print Solution().uniquePathsWithObstacles([[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]])