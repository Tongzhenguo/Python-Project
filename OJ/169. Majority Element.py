# coding=utf-8
__author__ = 'arachis'
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
找数组中的众数
众数投票算法（Boyer-Moore Algorithm ）：https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if( len(nums) == 1 ):
            return nums[0]
        ###init major and count
        major = 0
        count = 0
        for i in nums:
            if( count == 0 ):
                major = i
                count +=1
            elif( major == i ):
                count += 1
            else:
                count -= 1
        return major