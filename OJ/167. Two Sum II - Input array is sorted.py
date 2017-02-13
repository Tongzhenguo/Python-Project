# coding=utf-8
__author__ = 'arachis'

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
对于一个升序的整型数组，对于给定的值，找到数组中的两个数，它们的和是这个给定的值
The function twoSum should return indices of the two numbers such that they add up to the target,
 where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
返回的是以1开头的索引值，且index1 < index2 ，假定一定存在答案
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        二分查找
        """
        left , right = 0 , len(numbers) - 1
        while (left < right) :
            v = numbers[left] + numbers[right]
            if (v == target) :
                break
            elif (v > target):
                right -= 1
            else:
                left += 1
        return left+1,right+1
# print Solution().twoSum([-1,0],-1)
# print Solution().twoSum([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,4],7)
## Time Limit Exceeded
