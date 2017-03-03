# coding=utf-8
__author__ = 'arachis'
"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
统计字符串中词的长度，词与词之间是以空格分开的
Example:
Input: "Hello, my name is John"
Output: 5
"""
class Solution(object):
    def countSegments(self, s):
        """
        可以统计空格的个数，如果连续多个空格算一个,字符串开头和结尾中的空格不算
        结果就是空格数加一
        """
        s  = s.strip() #字符串开头和结尾中的空格不算
        if s == None or s == "":return 0
        space = 0
        for i in range( 1, len( s ) ,1 ):
            if( s[i] == " " and s[i-1] != " "): #如果连续多个空格算一个
                space += 1
        return space + 1

# print Solution().countSegments( "" )
# print Solution().countSegments( "     " )
# print Solution().countSegments( "Hello" )
# print Solution().countSegments( " Hello" )
# print Solution().countSegments( " Hello, my name is John" )