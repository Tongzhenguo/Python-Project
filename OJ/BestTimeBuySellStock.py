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
        找到一个较低的价格，并将当前利润和至今最大利润比较
        O(n),O(1)
        """
        buyPrice,profit = float("inf"),0
        for i in range(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i] ##找到一个低的价格
            if prices[i]-buyPrice > profit:
                profit = prices[i]-buyPrice ##更新最大利润
        return  profit

    def otherSolution(self,prices):
        """
        计算相邻的差值，然后就转换成了最大数组和问题(动态规划解法)
        O(n),O(1)
        """
        n = len(prices)
        profitSofar,maxProfit = 0,0
        for i in range(1,n,1):
            dpEndHere = (prices[i] - prices[i-1]) + (profitSofar if profitSofar>0 else 0)
            maxProfit = max(dpEndHere,maxProfit)
            profitSofar = dpEndHere
        return  maxProfit

# print Solution().otherSolution([7, 1, 5, 3, 6, 4])
# print Solution().otherSolution([7, 6, 4, 3, 1])
# print Solution().otherSolution([2,4,1])

# print Solution().maxProfit([7, 1, 5, 3, 6, 4])
# print Solution().maxProfit([7, 6, 4, 3, 1])
# print Solution().maxProfit([2,4,1])