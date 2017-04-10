# coding=utf-8
__author__ = 'arachis'
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
设计算法，在一个二维矩阵中搜索一个数
其中矩阵有如下特征：1.每行从左到右递增；每行的第一个数都比上一行最大的数大
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        先确定对应的行，然后行内二分查找
        """
        row_first = matrix[:,0]
        i = 0
        while( target>row_first[i] ):
            i += 1
        row  = i - 1
        low = 0
        high = len(matrix[0])-1
        while( low <= high ):
            mid = (low + high) / 2
            if( target==matrix[row][mid] ): return True
            if( target>matrix[row][mid] ):low = mid+1
            if( target<matrix[row][mid] ):high = mid-1
        return False