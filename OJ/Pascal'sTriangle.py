# coding=utf-8
__author__ = 'arachis'

"""
Given numRows, generate the first numRows of Pascal's triangle.
指定行数n，返回前n行的杨辉三角
For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
class Solution(object):
    def comb(self,n,i):
        res = 1.0
        for m in range(i):
            res *= n-m
        for m in range(i):
            res /= (i-m)
        return int(res)
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        resList = []
        for i in range(numRows):
            if i == 0:
                resList.append([1])
            else:
                pascalNums = []
                for j in range(i+1):
                    pascalNums.append(self.comb(i,j))
                resList.append(pascalNums)
        return resList
# print Solution().comb(7,5)
# print Solution().comb(4,2)
# print Solution().comb(3,3)
# print Solution().generate(1)
# print Solution().generate(3)
print Solution().generate(8)