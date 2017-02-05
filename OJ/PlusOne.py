# coding=utf-8
"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
以数字数组代表一个非负整数，返回加一后的数字数组
"""

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        jinwei,one = 0,1
        for i in range(n-1,-1,-1): ##两数相加，分别考虑本位和进位，而对于加一操作，进位即下次的本位
            lowVal = ((digits[i] - 0) + one) % 10
            jinwei = ((digits[i] - 0) + one) / 10
            digits[i] = lowVal
            one = 0 if jinwei == 0 else 1
        if one == 1:
            digits = [1] + digits
        return digits
# print Solution().plusOne([9,9])