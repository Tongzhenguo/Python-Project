# coding=utf-8
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
给定整型数组，计算i,j之间的和，约定i ≤ j，包括j
Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

# class NumArray(object):
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.array = nums
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return sum(self.array[i:j+1])


class NumArray(object):
    """
    DP问题练习：
    dp[i]:前i项和
    dp[0]=nums[0]
    dp[j>0]=dp[j-1]+nums[j]

    return dp[j]-dp[(i>1)-1]
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        dp = []
        if n!=0:
            dp.append(nums[0])
            for i in range(1,n,1):
                dp.append(dp[i-1]+nums[i])
        self.jsum = dp
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:return self.jsum[j]
        return self.jsum[j]-self.jsum[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray([-2, 0, 3, -5, 2, -1])
obj = NumArray([])
param_1 = obj.sumRange(1,2)
print param_1