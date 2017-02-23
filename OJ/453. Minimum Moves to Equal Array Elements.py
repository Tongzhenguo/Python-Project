# coding=utf-8
__author__ = 'arachis'

"""
Given a non-empty integer array of size n,
find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
由n个元素组成的整型数组，每一次对n-1个元素自增1，找到使得所有元素相等的最少变化次数
Example:
Input:
[1,2,3]
Output:
3
Explanation:
Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

class Solution(object):
    def minMoves(self, nums):
        """
        Incrementing all but one is equivalent to decrementing that one. So let's do that instead.
        How many single-element decrements to make all equal? No point to decrementing below the current minimum,
        so how many single-element decrements to make all equal to the current minimum?
        Just take the difference from what we currently have (the sum) to what we want (n times the minimum).
        """
        return sum(nums) - len(nums) * min(nums)
