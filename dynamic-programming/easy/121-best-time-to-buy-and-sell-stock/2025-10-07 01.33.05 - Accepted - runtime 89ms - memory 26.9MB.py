"""
LeetCode: 2025 10 07 01.33.05 Accepted Runtime 89ms Memory 26.9MB

Algorithm:
Iterate through each index.

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