# coding=utf-8
import math

__author__ = 'arachis'
"""
Given an integer, write a function to determine if it is a power of two.
判断一个数是不是2的幂
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        If an integer is power of 2, there is a single bit in the binary representation of n.
        e.g. 16 = b10000, 16 - 1 = b01111, and 16 & 16 - 1 = b10000 & b01111 = 0, also 16 != 0,
        based on these facts there is only one bit in b10000, so 16 is power of 2.
        """
        return n > 0 and not (n & n-1)