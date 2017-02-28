# coding=utf-8
__author__ = 'arachis'

"""
Reverse digits of an integer.
反转整数的存储，输入假定为32bit有符号整数；如果上溢则返回0
Example1: x = 123, return 321
Example2: x = -123, return -321
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        y=abs(x)
        string=str(y)
        result=int(string[::-1]) #反转字符串
        if result < 2147483648:
            if x<0:
                return -1*result
            else:
                return result
        else:
            return 0

# print Solution().reverse(-12)
# print Solution().reverse(233)