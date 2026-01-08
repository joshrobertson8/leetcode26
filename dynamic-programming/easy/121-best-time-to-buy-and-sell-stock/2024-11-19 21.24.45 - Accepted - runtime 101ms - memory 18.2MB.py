"""
LeetCode: 2024 11 19 21.24.45 Accepted Runtime 101ms Memory 18.2MB

Algorithm:
TODO: Describe your approach here

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