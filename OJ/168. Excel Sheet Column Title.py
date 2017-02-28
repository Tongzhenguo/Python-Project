# coding=utf-8
__author__ = 'arachis'
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
给一个正数，返回其在Excel表格中对应的编号
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
class Solution(object):
    def convertToTitle(self, n): #
        if n == 0:
            return ""
        else:
            n = n - 1 #从1开始，递归求进制转换
            return self.convertToTitle( n / 26) + chr( n % 26 + ord('A'))

# print Solution().convertToTitle( 28 )
# print Solution().convertToTitle( 26 )