# coding=utf-8
__author__ = 'arachis'
"""
Write a function to find the longest common prefix string amongst an array of strings.
写一个函数，找到一个字符串数组中最长公共前缀字符串
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        先找到长度最短的字符串s
        然后字符串数组各取出first n个字符去和s[:n]*len(strs)比较，直到不匹配返回
        """
        n = len(strs)
        minL = 100000000 #最短长度
        minS = ""
        if n == 0 :return ""
        for i in range( n ):
            if( len(strs[i]) < minL ):
                minL = len(strs[i])
                minS = strs[i]
        i = 0
        while( i < minL ):
            tmp = "".join( [ w[:i+1] for w in strs ] )
            if( not str(minS[:i+1]*n) == tmp ): #python == 用来判断两个对象的值是否相等
                return minS[:i] if i>0 else ""
            i += 1
        return minS

# print Solution().longestCommonPrefix( [] )
# # print Solution().longestCommonPrefix( ["a","ab","acc","ac"] )
# print Solution().longestCommonPrefix( ["a","b","c","d"] )
# print Solution().longestCommonPrefix( ["a","ab","aff","aos"] )