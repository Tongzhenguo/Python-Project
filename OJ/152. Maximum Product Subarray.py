# coding=utf-8
__author__ = 'arachis'

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
找最大子数组乘积（product）
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        maxhereSoFar,minhereSoFar = nums[0],nums[0]
        maxsofar = maxhereSoFar

        for i in range(1,len(nums),1):
            tmp = maxhereSoFar #上一次的最大值，去掉这个变量会影响逻辑
            maxhereSoFar = max(max(tmp * nums[i], minhereSoFar * nums[i]), nums[i]) ##当前绝对值最大的正数
            minhereSoFar = min(min(tmp * nums[i], minhereSoFar * nums[i]), nums[i]) ##当前绝对值最大的负数
            if maxhereSoFar > maxsofar: ##更新最大值
                maxsofar = maxhereSoFar
        return maxsofar
# print Solution().maxProduct([-2,-3,-4])
# print Solution().maxProduct([-4,-3])
# print Solution().maxProduct([-2,3,-4])
# print Solution().maxProduct([0,2])
# print Solution().maxProduct([0,-2])