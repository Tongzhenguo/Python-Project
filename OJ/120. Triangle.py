# coding=utf-8
__author__ = 'arachis'

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
给一个三角形，每个点都对应一个整型值，求从最顶行到最低行的最小和，约束每一步只能向下或者右下或者右下方移动
For example, given the following triangle
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
注：如果可以在O(N)空间复杂度下完成更好，N是总行数
"""

class Solution(object):
    #参考：https://leetcode.com/problems/triangle/?tab=Solutions
    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]

print Solution().minimumTotal([
    [-1],
    [2,3],
    [1,-1,-3]])