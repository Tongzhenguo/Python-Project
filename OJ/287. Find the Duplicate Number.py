# coding=utf-8
__author__ = 'arachis'
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
给一个长度是n+1的数组，每个元素x都在区间[1,n]之间，假设只有一个元素重复了两次。设计算法找到这个元素

链接：http://keithschwarz.com/interesting/code/?dir=find-duplicate
Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution(object):
    def findDuplicate(self, array):
        assert len(array) > 0

        # The "tortoise and hare" step.  We start at the end of the array and try
        # to find an intersection point in the cycle.
        slow = len(array) - 1
        fast = len(array) - 1

        # Keep advancing 'slow' by one step and 'fast' by two steps until they meet inside the loop.
        while True:
            slow = array[slow]
            fast = array[array[fast]]

            if slow == fast:
                break

        # Start up another pointer from the end of the array and march it forward
        #  until it hits the pointer inside the array.
        finder = len(array) - 1
        while True:
            slow   = array[slow]
            finder = array[finder]

            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow