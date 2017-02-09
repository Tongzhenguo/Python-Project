# coding=utf-8
__author__ = 'arachis'

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
给定二维01矩阵，找出含有全是由1组成的最大矩形面积
For example, given the following matrix:
["10100","10111","11111","10010"]
Return 6.
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        看的答案
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in xrange(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in xrange(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
print Solution().maximalRectangle(["10100","10111","11111","10010"])