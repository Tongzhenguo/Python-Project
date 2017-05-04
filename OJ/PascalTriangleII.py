# coding=utf-8
__author__ = 'arachis'

"""
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
简单翻译就是输入k,返回杨辉三角（Pascal's triangle）的第k层的元素

链接：https://leetcode.com/problems/pascals-triangle-ii/
杨辉三角维基百科：https://zh.wikipedia.org/wiki/杨辉三角形
"""
class Solution(object):
    def getNum(self,i, j):#这个回报超时
        # 计算a(i,j) = a(i-1,j-1)+a(i-1,j),行的首尾部分为1
        if(i==j or j==0):
            return 1
        return self.getNum(i-1,j-1)  + self.getNum(i-1,j)

    def comb(self,i, j):
        """
        a(i,j) 等于组合数 C（i，j），其中 i>=j>=0
        实现：comb(4,2) = val * 4/2 * 3/1
        当然可以调库scipy.special的comb
        """
        if (j == i or j == 0):##直接定义C(i,i)=C(i,0)=1
            return 1
        val = 1
        for k in xrange(i - j + 1, i + 1):
            val *= k
            val /= k-(i-j)
        return val

    def getRow(self, rowIndex):
        #解法：每一行对应的各元素就是Comb( rowIndex,i ),i从1到rowIndex
        res = [1] * (rowIndex+1)
        half = (rowIndex + 1) / 2
        for i in range(1, half+1,1):## 左右对称
            res[i] = self.comb(rowIndex,i)
            res[rowIndex-i] = res[i]
        return res

#this is a test
# print Solution().getRow(10)