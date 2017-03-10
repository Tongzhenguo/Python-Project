# coding=utf-8
__author__ = 'arachis'
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
海明距离是指两个整数的二进制比较中不同值的位的总数
例如，1和4的海明距离是2，因为第2,4位数值不同。
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        可以使用位运算中的异或，然后右移统计1的个数，直到结果为0
        """
        count = 0
        n = x ^ y
        while( n > 0 ):
            count += n % 2
            n = n >> 1
        return count
# print Solution().hammingDistance( 1,4 )