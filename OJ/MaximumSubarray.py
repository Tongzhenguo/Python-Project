# coding=utf-8
__author__ = 'arachis'

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
找到最大子数组和
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        动态规划解法(DP)，参考https://discuss.leetcode.com/topic/6413/dp-solution-some-thoughts/7
        """
        n,dpSolutionSoFar = len(nums),nums[0] ##当前dp问题最优解，初始化为第一个值
        maxSum = dpSolutionSoFar
        for i in range(1,n,1):
            dpSolutionEndHere = nums[i] + (dpSolutionSoFar if dpSolutionSoFar > 0 else 0) #状态转移方程（递推式），如果之前最优解为0就抛弃，否则保存
            maxSum,dpSolutionSoFar = max(maxSum, dpSolutionEndHere),dpSolutionEndHere ##更新
        return maxSum
print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])