# coding=utf-8
"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
给定非空正整数数组，判断是否能找到一个子集，这个子集的和为数组和的一半
"""

class Solution(object):
    # def canPartition(self, nums):
        """
        DP练习：
        dp[i][j]:sum(nums[:i+1])==j
        dp[0][0]=True
        dp[i][0]=True ##为什么不是False?
        dp[0][j]=False
        dp[i>0][j>0] = dp[i-1][j] #不选择nums[i]
        dp[i>0][j>0] = dp[i-1][j-nums[i-1]] #选择nums[i]
        """
        # n = len(nums)
        # sumn = sum(nums)
        # if sumn%2!=0:return False
        # sumn /= 2
        # dp = [[] for i in range(n+1)]
        # for i in range(n+1):
        #     dp[i] = [False]*(sumn+1)
        #     for j in range(sumn+1):
        #         if(i==0):
        #             if(j==0):
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = False
        #         elif(j==0):
        #             dp[i][j] = True
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        #             if(j-nums[i-1]>=0):
        #                 dp[i][j] = (dp[i][j] or dp[i-1][j-nums[i-1]] ) #两种情况，有一成功就可以
        # return dp[n][sumn]
# print Solution().canPartition([1,5,11,5])
# print Solution().canPartition([1,2,5])
        def canPartition(self, nums):
            """
            优化空间O(1)
            dp[i][j]:sum(nums[:i+1])==j
            dp[0]=True
            dp[j>0] = dp[j] or dp[j-nums[i-1]]
            """
            sumn = sum(nums)
            if sumn % 2 != 0: return False
            sumn /= 2
            dp = [False] * (sumn + 1)
            dp[0] = True
            for num in nums:
                for j in range(sumn,0,-1): ##倒着回滚
                    if j >= num:
                        dp[j] = (dp[j] or dp[j - num])  #更新
            return dp[sumn]
# print Solution().canPartition([1,5,11,5])
# print Solution().canPartition([1,2,5])
