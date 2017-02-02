# coding=utf-8
__author__ = 'arachis'

"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
简单翻译就是数组nums循环右移k位，返回原地变换(不允许进行移动) 的结果
https://zh.wikipedia.org/zh-cn/原地算法 list.reverse()
"""
class Solution(object):
    # def inverse(self,nums,start,stop):
    #     left,right = start,stop
    #     while(left < right):
    #         tmp = nums[left]
    #         nums[left] = nums[right]
    #         nums[right] = tmp
    #         left += 1
    #         right -= 1
    #     return nums
    # def rotate(self, nums, k):
    #     """
    #     分三次翻转可以得到最终结果，
    #     """
    #     n = len(nums)
    #     k %= n
    #     if(k != 0):  #k == 0 means not change
    #         self.inverse(nums,0,n-k-1)
    #         self.inverse(nums,n-k,n-1)
    #         self.inverse(nums,0,n-1)
    def rotate(self,nums,k):
        n = len(nums)
        k %= n
        if(k != 0):  #k == 0 means not change
            for i in range(n-1,0,-1):
                tmp = nums[(i+k)%n]
                nums[(i+k)%n] = nums[i]
                nums[i] = tmp
        return nums

print Solution().rotate([1,2,3,4,5],2)
print Solution().rotate([1,2,3,4,5],7)
print Solution().rotate([1],2)