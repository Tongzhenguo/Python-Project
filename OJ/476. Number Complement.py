# coding=utf-8
"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
求一个正数的补数，补数的定义是两个数对应的二进制位完全相反，注1的补数是0，数字都是int32
Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""
class Solution(object):
    def findComplement(self, num):
        """
        直接数值计算，补数有如下规律：假设a,b互为补数，则他们的和是相同位数能表示的2进制最大值
        所以关键就是求两个数的二进制位数，同样可以使用右移确定
        """
        count = 0
        n = num
        while( num > 0 ):
            count += 1
            num = num >> 1
        return 2 ** count - 1 - n

print Solution().findComplement(5)
print Solution().findComplement(1)
