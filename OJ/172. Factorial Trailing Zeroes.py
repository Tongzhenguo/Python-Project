# coding=utf-8
__author__ = 'arachis'
"""
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
计算n!中尾随0的个数，要求时间是O(logN)
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        Because all trailing 0 is from factors 5 * 2.
        But sometimes one number may have several 5 factors,for example, 25 have two 5 factors, 125 have three 5 factors.
        In the n! operation, factors 2 is always ample(充足的). So we just count how many 5 factors in all number from 1 to n.
        比如1 to 120 ,肯定有120/5个因子为5的因子，然后再去讨论可以被5整除两次，三次，。。。
        """
        if n <= 0:return 0
        else: # f(n) = n/5 + f(n/5)
            n / 5 + self.trailingZeroes(n / 5) #top1 solution

# print Solution().trailingZeroes(120) #28
# print Solution().trailingZeroes(30)
