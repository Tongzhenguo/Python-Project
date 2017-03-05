# coding=utf-8
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
给一句话，求最后一个词的长度，如果不存在最后一个词，返回0
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        """
        s = s.strip()
        if s == "": return 0
        count = 0
        i = len(s)-1
        while( i>=0 ):
            if( s[i] != " " ):
                count += 1
                i -= 1
            else:
                break
        return count

# print Solution().lengthOfLastWord(" ")
# print Solution().lengthOfLastWord("")
# print Solution().lengthOfLastWord("Hello World")