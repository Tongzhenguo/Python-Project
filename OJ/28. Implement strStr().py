# coding=utf-8
__author__ = 'arachis'
"""
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
needle:针
haystack：大海
自己实现方法，查找字符串中某模式第一次出现的索引，没有返回-1
"""
class Solution(object):
    def strStr(self, haystack, needle):
         for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle: #滑动窗口匹配
                return i
         return -1

# print Solution().strStr( "","" )
# print Solution().strStr( "a","" )
# print Solution().strStr( "a","a" )
# print Solution().strStr( "aabbabb","bba" )
# print Solution().strStr( "mississippi","issip" )