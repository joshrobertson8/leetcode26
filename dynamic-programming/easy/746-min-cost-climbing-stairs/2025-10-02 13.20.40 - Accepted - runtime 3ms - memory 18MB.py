"""
LeetCode: 2025 10 02 13.20.40 Accepted Runtime 3ms Memory 18MB

Algorithm:
Dynamic programming backwards: dp[i] represents minimum cost from step i to top. Initialize dp[n-1] = cost[n-1], dp[n-2] = cost[n-2]. For each step i from n-3 down to 0, dp[i] = cost[i] + min(dp[i+1], dp[i+2]). Return min(dp[0], dp[1]) since we can start from step 0 or 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 0: return 0
        if n == 1: return cost[0]

        dp = [0] * n
        dp[n - 1] = cost[n - 1]
        dp[n - 2] = cost[n - 2]
        
        for i in range(n - 3, -1, -1):
            dp[i] = (cost[i] + min(dp[i + 1], dp[i + 2]))

        return min(dp[0], dp[1])