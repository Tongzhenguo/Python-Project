# coding=utf-8
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
将有序数组num1（长度为m） 和 nums2（长度为n）,将nums2 归并到nums1并保证有序（原地算法）
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
         插入排序
        """
        for i in range(n):
            j = m - 1
            while(j>=0 and nums1[j] > nums2[i]): ##move backword
                nums1[j+1] = nums1[j]
                j -= 1
            nums1[j+1] = nums2[i]  ## insert
            m += 1
            # return nums1
    def topSolution(self,nums1, m, nums2, n):
        i,j,k = m-1,n-1,m+n-1
        while(i>=0 and j>=0):#从后依次比较，大者后移
            if(nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while(j>=0):
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        return nums1
print Solution().topSolution([1,0],1,[2],1)