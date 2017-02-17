# coding=utf-8
__author__ = 'arachis'

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
对两个字符串s,t>0；找到s中以p或者的p异序词开头的索引，字符串都是小写英文的
Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        滑动窗口 (i-m,i)
        每次移动都比较下个字符串的hash数组值，如果完全相等就代表s的滑动窗口内和p的元素完全相同
        可以通过这个题再次思考《数学之美》中的信息指纹那一章
        """
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0]*123, [0]*123 #对应ascii码的出现次数
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m-1]:
            shash[ord(x)] += 1
        for i in range(m-1, n):
            shash[ord(s[i])] += 1
            if i-m >= 0:#左边界的元素上次已经在窗口内，出现次数减一
                shash[ord(s[i-m])] -= 1
            if shash == phash:#右边界的元素是新增的，出现次数加一
                res.append(i - m + 1)
        return res

# print Solution().findAnagrams("cbaebabacd"
# ,"abc")
