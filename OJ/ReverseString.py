# coding=utf-8
"""
 Write a function that takes a string as input and returns the string reversed.
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sbytes = bytearray(bytes(s))
        left = 0
        right = len(sbytes) - 1
        while(left<right):
            tmp = sbytes[left]
            sbytes[left] = sbytes[right]
            sbytes[right] = tmp
            left +=1  ##原来Python早就放弃了自增运算符！
            right -=1
        return str(sbytes)
    print reverseString(object,'abc')
    print reverseString(object,'hello!')

