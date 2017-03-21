# coding=utf-8
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
题意是n=1时输出字符串1；
n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；
n=3时，由于上次字符是11，有2个1，所以输出21；
n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。依次类推
Note: The sequence of integers will be represented as a string.
"""

class Solution(object):
    def countAndSay(self, n):
        if n == 1:return "1"
        tmp = self.countAndSay(n-1)+"*" #便于处理末尾
        res = ""
        count = 0
        for i in range(len(tmp)-1):
            if tmp[i] == tmp[i+1]:#相同则统计
                count += 1
            else: #不同输出上一个，重置统计当前
                res += str(count+1) + tmp[i]
                count = 0 #reset
        return res

# print Solution().countAndSay( 1 )
# print Solution().countAndSay( 3 )
# print Solution().countAndSay( 5 )
# print Solution().countAndSay( 1000 )