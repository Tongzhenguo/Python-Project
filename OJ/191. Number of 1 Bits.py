# coding=utf-8
__author__ = 'arachis'
"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
给一个无符号整数，求这个数的二进制中1的个数，也叫海明权重
For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""
class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while( n > 0 ):
            count += n % 2
            n /= 2
        return count
# print Solution().hammingWeight( 11 )
# print Solution().hammingWeight( 0 )
# print Solution().hammingWeight( 255 )
# print Solution().hammingWeight( 2 ** 31 - 1 )