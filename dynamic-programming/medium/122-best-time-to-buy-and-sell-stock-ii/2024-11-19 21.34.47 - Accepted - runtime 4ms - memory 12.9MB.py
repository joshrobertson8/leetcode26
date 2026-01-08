"""
LeetCode: 2024 11 19 21.34.47 Accepted Runtime 4ms Memory 12.9MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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