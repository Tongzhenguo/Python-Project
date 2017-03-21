# coding=utf-8
__author__ = 'arachis'
"""
Given two binary strings, return their sum (also a binary string).
计算两个二进制字符串表示整数的和，结果也用二进制字符串表示
For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        m,n = len(a),len(b)
        res = [0] * ( max( m,n )+1 )
        if( m<n ): #保证位数相同
            a = (n - m)*"0" + a
        if( m>n ):
            b = (m - n)*"0" + b
        tmp = 0 #中间进位
        for i in range( len(a)-1 , -1 , -1 ):
            k = int(a[i])+int(b[i])+tmp
            res[i+1] = k % 2
            tmp = 1 if k >=2 else 0
        if tmp == 1: #处理最高位
            res[0] = 1
            return "".join(map(str,res))
        return "".join(map(str,res[1:]))
# print Solution().addBinary("11",'1')
# print Solution().addBinary("111","1")
# print Solution().addBinary("0","1000")