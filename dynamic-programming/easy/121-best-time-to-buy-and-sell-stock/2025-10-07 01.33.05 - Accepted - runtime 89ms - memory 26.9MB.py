"""
LeetCode: 2025 10 07 01.33.05 Accepted Runtime 89ms Memory 26.9MB

Algorithm:
Track the minimum buy price seen so far (buyPoint). For each day, if the current price is lower than buyPoint, update buyPoint. Calculate profit if selling today (price - buyPoint) and update the maximum profit. This finds the best single buy-sell pair in one pass.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curMax = 0

        if not prices: 
            return 0
        
        buyPoint = float('inf')

        for i in range(len(prices)): 

            if prices[i] < buyPoint: 
                buyPoint = prices[i]

            curMax = max(curMax, prices[i] - buyPoint)

        return curMax