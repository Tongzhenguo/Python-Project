# coding=utf-8
__author__ = 'arachis'

"""
Determine whether an integer is a palindrome. Do this without extra space.
判断一个整数是不是回文，不能使用额外内存
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        低位数字和高位数字比较
        """
        n = len(str(x))
        if x < 0:return False
        if n==1:return True
        for i in range(1,n/2+1,1 ):
            low = x % (10 ** i) / (10 ** (i - 1))  #(9999 % 10 )/ 1
            high = x % (10 ** (n-i+1)) / (10 ** (n-i)) # (9999 % 10000 )/ 1000
            if ( low !=  high ):
                return False
        return True
# print Solution().isPalindrome(111)
# print Solution().isPalindrome(10)
# print Solution().isPalindrome(-77)
# print Solution().isPalindrome(19999)
# print Solution().isPalindrome(9999) # 9999 / 100 ==  9999 % 100

