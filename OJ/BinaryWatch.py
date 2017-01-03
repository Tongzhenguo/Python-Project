# coding=utf-8
__author__ = 'arachis'

"""
题目大意：
一个二进制手表顶端有4盏LED灯表示小时(0-11)，底部有6盏LED灯表示分钟(0-59)。
每一盏LED灯表示一个0或1，最右端为最低位。

给定一个非负整数n表示当前燃亮的LED灯数，返回所有可能表示的时间。
"""
class Solution(object):
    """
        注：从网上get的方法（http://bookshadow.com/weblog/2016/09/18/leetcode-binary-watch/）
    """
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if(bin(h)+bin(m)).count('1') == num:
                    res.append("%d:%02d" % (h,m))
        return res

##this is a test
print Solution().readBinaryWatch(2)