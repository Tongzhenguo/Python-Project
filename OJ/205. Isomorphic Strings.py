# coding=utf-8
"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.No two characters may map to the same character but a character may map to itself.

isomorphic:同形的
如果两个字符串是同种结构的，就称为他们是同形的，写算法判断是否是同形字符串
假定两个字符串的长度相同
For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        思路来自290. Word Pattern
        """
        return map(s.find,s) == map(t.find,t)

# print Solution().isIsomorphic("egg", "add")
# print Solution().isIsomorphic("foo", "bar")
# print Solution().isIsomorphic("paper", "title")