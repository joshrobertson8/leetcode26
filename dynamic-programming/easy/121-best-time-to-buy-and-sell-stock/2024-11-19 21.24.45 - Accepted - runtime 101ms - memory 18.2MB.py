"""
LeetCode: 2024 11 19 21.24.45 Accepted Runtime 101ms Memory 18.2MB

Algorithm:
Track the minimum buy price seen so far (buy_in). For each price, update buy_in to the minimum, calculate profit if selling today (price - buy_in), and update max_profit. This finds the best single buy-sell pair in one pass.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy_in = float('inf')
        max_profit = 0

        for price in prices:

            buy_in = min(buy_in, price)

            profit = price - buy_in

            max_profit = max(max_profit, profit)
        
        return max_profit