# coding=utf-8
"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:
购买股票最大收益问题，每天都会交易或者在冷静期，但是要想购买只能先全部卖出，并且在第二天不能购买
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        DP问题练习：
        dp1[i]:第i天卖出可能达到的最大收益
        dp2[i]:第i天什么也不做可能达到的最大收益
        dp1[0]=0
        dp2[0]=0
        dp1[i>0]= max(dp2[i-1],prices[i]-prices[i-1])
        dp2[i>0]= max(dp1[i-1],dp2[i-1])
        空间可以优化成O(1)
        """
        n = len(prices)
        if n==0:return 0
        profit1 =0
        profit2 =0
        for i in range(1,n,1):
            copy = profit1
            profit1 = max(profit1 + prices[i] - prices[i - 1], profit2)
            profit2 = max(copy, profit2)
        return max(profit1,profit2)
print Solution().maxProfit([1, 2, 3, 0, 2])