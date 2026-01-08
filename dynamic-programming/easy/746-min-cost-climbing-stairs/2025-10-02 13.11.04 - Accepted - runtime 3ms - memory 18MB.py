"""
LeetCode: 2025 10 02 13.11.04 Accepted Runtime 3ms Memory 18MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 0: return 0
        if n == 1: return arr[0]

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = (cost[i] + min(dp[i - 1], dp[i - 2]))

        return min(dp[n - 1], dp[n - 2])