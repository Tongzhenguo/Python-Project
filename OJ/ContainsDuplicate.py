# coding=utf-8
"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
 and it should return false if every element is distinct.

简单翻译就是给你一个整型数组，如果有重复就返回true,否则为false
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## func1
        # s = set(nums)
        # return len(s) != len(nums)

        ## func2
        # sortedNums = sorted(nums)
        # for i in range( len(sortedNums)-1 ):
        #     if(sortedNums[i] == sortedNums[i+1] ):
        #         return True
        # return False

        ## func3 :边插入，边判断
        s = set()
        for n in nums:
            if(s.__contains__(n)):
                return True
            s.add(n)
        return False

import datetime
start = datetime.datetime.now()
print (Solution().containsDuplicate(10000000*[1, 2, 3, 4, 5, 6,7,8,9,10,1,10]))
print (datetime.datetime.now() - start).seconds ##45s for func 2 ,4s for func1



