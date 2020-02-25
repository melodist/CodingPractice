"""
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Max profit is equal to the sum of the consecutive peak.
"""
class Solution:     
    def maxProfit(self, prices):
        """
        :type List[int]
        :rtype int
        """
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        
        return profit
