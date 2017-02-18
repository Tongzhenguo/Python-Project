# coding=utf-8
"""
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
对于一个由大小写字母组成的字符串，通过字符串中的任意字母构造一个最长的回文，求回文的长度
Note:
Assume the length of given string will not exceed 1,010.

"""
class Solution(object):
    def longestPalindrome(self, s):
        sList = list(s)
        aDict = {}
        length = 0
        for alpha in sList:
            aDict[ alpha ] = aDict.get(alpha,0) + 1
        sorted1 = sorted(aDict.iteritems(), key=lambda p: p[1], reverse=True)
        oddExist = False #回文的中间放奇数个字母
        for item in sorted1:
            if(item[1] %2 == 0):
                length += item[1]
            else:
                length += item[1]-1 #挑出偶数个
                oddExist = True
        if oddExist: length += 1
        return length

# print Solution().longestPalindrome("abccccdd")
# print Solution().longestPalindrome("zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez")
# print Solution().longestPalindrome("bb")