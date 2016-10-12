class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 如果只有一个数直接返回。否则将所有数异或出来的值就是单数
        length = len(nums)
        if(length == 1):
            return nums[0]
        else:
            for i in range(1,length):
                nums[0] ^= nums[i]
            return nums[0]
