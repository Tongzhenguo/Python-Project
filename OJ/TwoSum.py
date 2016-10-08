"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {} ###空字典
        idxs = [] ###空列表
        length = len(nums) ##求长度
        for i in range(length):
            dict[nums[i]] =i ###读列表，存字典
        for i in range(length):# 返回0 to length -1
            if(dict.get(target - nums[i]) != None):##python 中的None
                j = dict.get(target - nums[i])
                if(j != i):
                    idxs.append(i) ##写列表
                    idxs.append(j)
                    break
        return idxs
    print twoSum(object,[1,2,3],4)