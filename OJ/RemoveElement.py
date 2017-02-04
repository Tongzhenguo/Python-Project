# coding=utf-8
__author__ = 'arachis'

"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
给定数组和元素，求出去掉指定元素的数组长度，要求使用原地算法
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
"""

class Solution(object):
    def removeElement(self, nums, val):
        n,i = len(nums),0
        while(i<n):##if equals,replace the num with the last num and update the length of nums
            if nums[i] == val:
                nums[i] = nums[n-1]
                i -= 1
                n -= 1
            i += 1
        return n
# print Solution().removeElement([2,2,3],3)