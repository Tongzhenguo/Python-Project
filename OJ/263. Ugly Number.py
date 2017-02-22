# coding=utf-8
import math

__author__ = 'arachis'
"""
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
Ugly numbers 是说一个只能有质因子2,3,5的正整数，写一个算法判断是不是Ugly numbers
Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
    def isUgly(self, num):
        """
        一直判断能不能对2,3,5整除，直到除尽或者不在范围
        """
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1

print Solution().isUgly(4)

