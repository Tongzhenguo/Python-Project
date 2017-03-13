# coding=utf-8
"""
Reverse bits of a given 32 bits unsigned integer.
给一个无符号的32位整数，返回其对应二进制字符串左右反转了的数字，注：这个函数可能会多次被调用，是否能优化
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution:
    def reverseBits(self, n):
        i = 0
        result = 0
        while( n>0 ):
            result += (n % 2) * (2 ** (32 - 1 - i))
            i += 1
            n = n >> 1
        return result

print Solution().reverseBits(43261596)
# print Solution().reverseBits(0)
# print Solution().reverseBits(2 ** 16)