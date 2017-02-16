# coding=utf-8
__author__ = 'arachis'

"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
给定一个矩阵代表的网格，其中1代表陆地，0代表海洋；网络是以水平或者垂直连接的；这些陆地连成了一个小岛
每一块陆地的都是边为1的正方形，求小岛的周长
Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        判断一个陆地的四周是否被水覆盖，挨着水的计入边长
        """
        m,n = len(grid),len(grid[0])
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:continue
                c += 4
                if i>0: c -= grid[i-1][j]
                if i<m-1: c -= grid[i+1][j]
                if j>0: c -= grid[i][j-1]
                if j<n-1: c -= grid[i][j+1]
        return c
print Solution().islandPerimeter(
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]])