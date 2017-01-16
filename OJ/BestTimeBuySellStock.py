# coding=utf-8
__author__ = 'arachis'

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

简单翻译就是已知一只股票每天的价格，求最大收益
例1：
Input: [7, 1, 5, 3, 6, 4]
Output: 5
例2：
Input: [7, 6, 4, 3, 1]
Output: 0
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyPrice = float("inf")
        profit = 0
        for i in xrange(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            if prices[i]-buyPrice > profit:
                profit = prices[i]-buyPrice
        return  profit
# print Solution().maxProfit([7, 1, 5, 3, 6, 4])
# print Solution().maxProfit([7, 6, 4, 3, 1])
# print Solution().maxProfit([2,4,1])