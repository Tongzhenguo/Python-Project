# coding=utf-8
__author__ = 'arachis'

"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k)
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
pairwise:成对的    boomerang：回转棒
一个回转数（i,j,k）就是
平面上n个点，一个回转数（i,j,k）就是点i,j距离等于点i,k的距离,找到回转数的个数
点的个数n<=500,平面的最大区间是[-10000, 10000]
Example:
Input:
[[0,0],[1,0],[2,0]]
Output:
2
Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        记录两点距离的统计值

        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res

