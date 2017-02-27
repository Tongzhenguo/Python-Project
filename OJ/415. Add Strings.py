# coding=utf-8
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
给两个以字符串（<5100）代表的正整数，求两个正整数的和
注：不应该考虑调用库函数
Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        低位对齐，高位补零
        低位1，低位2，上一次进位
        """
        n1,n2 = len(num1), len(num2)
        if n1 > n2:
            num2 = (n1-n2) * "0" + num2
        if n1 < n2:
            num1 = (n2 - n1) * "0" + num1
        tmp = 0 #进位
        res = [0] * ( len(num1)+1 )
        for i in range(len(num1)-1,-1,-1):
            t = int(num1[i])+int(num2[i])+tmp
            res[i+1] = t % 10
            tmp =1 if t>9 else 0
        if ( tmp > 0):
            res[0] = 1
        else:
            res = res[1:]
        return "".join( map(str,res) )

print Solution().addStrings("408","5")
# print Solution().addStrings("11111","99999")
# print Solution().addStrings("11111"*1000,"99999")