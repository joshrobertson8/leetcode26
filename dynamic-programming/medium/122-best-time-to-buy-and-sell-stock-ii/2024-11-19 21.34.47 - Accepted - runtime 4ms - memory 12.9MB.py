"""
LeetCode: 2024 11 19 21.34.47 Accepted Runtime 4ms Memory 12.9MB

Algorithm:
Greedy approach: capture every profit opportunity. For each consecutive pair of days, if tomorrow's price is higher than today's, buy today and sell tomorrow, adding the profit. This maximizes total profit by capturing all upward price movements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        
        for price in range(len(prices) - 1):
            if prices[price] < prices[price + 1]:
                max_profit += prices[price + 1] - prices[price]
            
        return max_profit