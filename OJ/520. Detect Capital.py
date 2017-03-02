# coding=utf-8
__author__ = 'arachis'
"""
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
当一个大写字母出现在单词中，正确的情况有如下：
1.全部字母都是大写
2.全部字母中没有一个大写
3.如果不止一个字母，只有首字母可以大写
否则就是错误大写

Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False

"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        """
        n = len( word )
        if n == 1:return True
        if word[0].isupper():
            i = 1
            while( i<n  and word[i].isupper()):
                i += 1
            if i == n:#rule 1
                return True
            i = 1
            while(  i<n and not word[i].isupper() ):
                i += 1
            if i == n:#rule 3
                return True
        else:
            i = 0
            while( i<n and (not word[i].isupper() )  ):
                i += 1
            if i == n:#rule 2
                return True
        return False

# print Solution().detectCapitalUse( "aT" )
# print Solution().detectCapitalUse( "TAAA" )
# print Solution().detectCapitalUse( "Aaaa" )
# print Solution().detectCapitalUse( "aaaa" )
# print Solution().detectCapitalUse( "aaAa" )