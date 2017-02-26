# coding=utf-8
"""
Given an integer, write a function to determine if it is a power of three.
判断给定整数是否是3的幂;思考是否可以不用循环或者递归
Follow up:
Could you do it without using any loop / recursion?
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        """
        if n <= 0:return False
        while( n % 3 == 0 ):
            n /= 3
        return n == 1

class Solution(object):
    def isPowerOfThree(self, n):
        #3是素数,所以可以证明3 ** k的质因子只有3
        # 1162261467 is 3 ^ 19, 3 ^ 20 is bigger than int
        return (n > 0 and  1162261467 % n == 0)