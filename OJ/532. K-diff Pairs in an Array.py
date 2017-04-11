# coding=utf-8
__author__ = 'arachis'

"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
定义k-diff pair是两个绝对值距离等于K的，属于同一个数组的值
给定整型数组和一个K,设计算法计算：k-diff pair的个数

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
"""
class Solution(object):
    def findPairs(self, nums, k):
        """主要是考虑去重，存一个set
        """
        if (nums==None or len(nums)==0 or k < 0): return 0
        map = {}
        count = 0
        for i in  nums:
            map[i] =  1+ map.get(i, 0)
        for entry in map.iteritems():
            if (k == 0) :
                #count how many elements in the array that appear more than twice.
                if (entry[1] >= 2):
                    count += 1
            else:
                if (map.__contains__(entry[0] + k)):
                    count +=1
        return count

print Solution().findPairs([3,1,4,1,5],2)