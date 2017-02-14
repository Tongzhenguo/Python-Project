# coding=utf-8
__author__ = 'arachis'

"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
给定一个模式和一个字符串，判断是否是完全匹配的
假定都是小写字母，并且字符串以空格分开
Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        map的api:
            args1：迭代函数
            args2: 可迭代的序列
        """
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t) #如果第一次出现的位置和字符串数组的下标相同，匹配成功
# print Solution().wordPattern("abba","dog cat cat dog")
# print Solution().wordPattern("abba","dog cat cat fish")
# print Solution().wordPattern("jquery","jquery")
print Solution().wordPattern("abba","cat cat cat cat")