# coding=utf-8
__author__ = 'arachis'

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def biSearch(self,nums,target,left,right):
        if(right - left <= 1):
            return right ##递归出口1,当左右边界中间没有元素时，返回右者

        mid = ( left + right ) / 2
        if(target < nums[mid]):
            return self.biSearch(nums,target,left,mid)
        elif(target == nums[mid]):
            return mid  ##递归出口2,返回元素出现的位置
        else:
            return self.biSearch(nums,target,mid,right)

    def searchInsert(self, nums, target):
        n = len(nums)
        if(target <=nums[0]):
            return 0 ##比数组中最小的还小，直接返回
        elif(target > nums[n-1]):
            return n ##比数组中最大的还大，返回
        else:## 如果介于nums[0] 和 nums[n-1]之间，则二分查找
            left,right = 0,n-1
            return self.biSearch(nums,target,left,right)


    def topSolution(self,nums,target):
        n = len(nums)
        left,right = 0,n-1
        while(left <= right):
            mid = ( left + right ) / 2
            if(target == nums[mid]):return mid  ##1:return the index of target
            if(target < nums[mid]):
                right = mid-1
            else:
                left = mid+1
        return right ##2:target not exist,return position

# print Solution().searchInsert([1,3,5,6], 2 )
# print Solution().searchInsert([1],0 )