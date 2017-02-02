# coding=utf-8
__author__ = 'arachis'

"""
    Given a non-empty array of integers, return the third maximum number in this array.
    If it does not exist, return the maximum number.
    The time complexity must be in O(n).
    简单翻译就是求整型非空数组的第三大元素，如果不存在就返回top1,要求时间复杂度为O(n),另这里第三不包括重复
    leetcode 上直接看的答案“Java neat and easy understand solution, O(n) time, O(1) space”
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        这里理解下就是三个元素的数组分别存储最大的三个数，如果有比其中一个大的就依次右移，将新数插入这个位置
        注：这里判断顺序不能变，先和最大的比
        """
        tops = [float("-inf")] * 3
        for i in nums:
            if(i>tops[0]):
                tops[2] = tops[1]
                tops[1] = tops[0]
                tops[0] = i
            if(i>tops[1] and i<tops[0]):
                tops[2] = tops[1]
                tops[1] = i
            if(i>tops[2] and i<tops[1]):
                tops[2] = i
        return tops[2] if tops[2] > float("-inf") else tops[0]
# print Solution().thirdMax([1,1,1,1])
# print Solution().thirdMax([1,2,2,3])
# print Solution().thirdMax([2, 2, 3])





