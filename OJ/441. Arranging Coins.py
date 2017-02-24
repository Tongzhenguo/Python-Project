# coding=utf-8
import math

__author__ = 'arachis'
"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.
假定你有n（>0）个硬币，想要摆成一个楼梯状，第k(>0)行有k个硬币数。返回可以可摆成最高的楼梯层数。
Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        等差数列，第n阶以下的总硬币数 S(n) = (1+n)*n / 2
        反过来n的解为 n = -0.5 * [ 1 + sqrt(1+8y) ]
        """
        return int( 0.5 * ( -1 + math.sqrt(1+8*n) )  )
# print Solution().arrangeCoins( 5 )
# print Solution().arrangeCoins( 8 )
# print Solution().arrangeCoins( 3 )