# coding=utf-8
__author__ = 'arachis'

"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
单股最大受益问题，一天可以多次交易，但只能全买或者全卖
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        这么简单我也没做出来啊，题目确实设计的有点问题
        """
        total = 0
        for i in range(len(prices)-1):
            if (prices[i+1]-prices[i]>0):
                total += prices[i+1]-prices[i]
        return total
print Solution().maxProfit([1,2,5,1])
