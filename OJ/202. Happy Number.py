# coding=utf-8
__author__ = 'arachis'

"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process:
 Starting with any positive integer, replace the number by the sum of the squares of its digits,
 and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
写一个算法判断是否是“happy”
一个“happy”的数是以正数开始，用每一位的数字的平方和替换这个数，迭代直到最后这个数等于1的数，否则不是。
Example: 19 is a happy number
"""

class Solution(object):
    def isHappy(self, n):
        """
        """
        sumdigitS = 0
        N = 0
        while( n > 0 ):
            sumdigitS += ( n % 10 ) ** 2
            print sumdigitS
            n /= 10
            if n == 0:
                N += 1
                n = sumdigitS
                sumdigitS = 0
                if n == 1:return True
                if N == 100:return False
# print Solution().isHappy(19)
# print Solution().isHappy(999)