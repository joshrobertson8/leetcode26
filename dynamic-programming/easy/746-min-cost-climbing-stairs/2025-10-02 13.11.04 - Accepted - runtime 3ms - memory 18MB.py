"""
LeetCode: 2025 10 02 13.11.04 Accepted Runtime 3ms Memory 18MB

Algorithm:
Dynamic programming: dp[i] represents minimum cost to reach step i. Initialize dp[0] = cost[0], dp[1] = cost[1]. For each step i >= 2, dp[i] = cost[i] + min(dp[i-1], dp[i-2]). Return min(dp[n-1], dp[n-2]) since we can reach top from either of last two steps.

Time Complexity: O(n)
Space Complexity: O(1)
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