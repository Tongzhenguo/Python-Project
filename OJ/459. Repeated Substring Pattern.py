# coding=utf-8
"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
给定一个非空的字符串，假定都是小写字母；判断这个字符串是否是其子串的n次重复构成的

"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """和数组最大前缀解放基本相同
        """
        n = len(s)
        for i in range( n-1 ):
            if( n % (i+1) == 0 and s[:i+1] * ( n / (i+1) ) == s ):
                return True
        return False

# print Solution().repeatedSubstringPattern( "abab" )
# print Solution().repeatedSubstringPattern( "aba" )
# print Solution().repeatedSubstringPattern( "abcabcabcabc" )
# print Solution().repeatedSubstringPattern( "abab" )