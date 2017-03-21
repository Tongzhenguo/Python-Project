# coding=utf-8
__author__ = 'arachis'
"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
给一个罗马数字表示的整数，转换成阿拉伯数字
"""

class Solution(object):
    def romanToInt(self, s):
        """
        """
        numMap = { 'I':1 , 'V':5 ,'X':10 ,'L':50 , 'C':100 , 'D':500, 'M':1000 }
        n = len(s)
        res = 0
        i = 0
        while(i < n-1 ):
            key1 = s[i]
            key2 = s[i+1]
            if numMap[key1] < numMap[key2]: #IV = -1 + 5
                res -= numMap[key1]
            else:
                res += numMap[ key1 ]
            i += 1
        res += numMap[ s[n-1] ] #加上最后一位
        return res
# print Solution().romanToInt("III") #
# print Solution().romanToInt("IV")
# print Solution().romanToInt("MCMXCVI")
# print Solution().romanToInt("CMXCVI")

