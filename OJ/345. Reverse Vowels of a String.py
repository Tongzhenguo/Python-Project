# coding=utf-8
__author__ = 'arachis'
"""
Write a function that takes a string as input and reverse only the vowels of a string.
vowels:元音，a,e,i,o,u
将一个字符串的元音部分进行反转
Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""
class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u']
        p = 0
        q = len(s)-1
        res = list(s)
        while( p <q ):
            if( vowels.__contains__(s[p].lower()) ):
                if( vowels.__contains__(s[q].lower())  ):
                    res[p] = s[q]
                    res[q] = s[p]
                    p += 1
                    q -= 1
                else:
                    q -= 1
            else:
                p += 1
        return "".join(res)
print Solution().reverseVowels("lEetcode")