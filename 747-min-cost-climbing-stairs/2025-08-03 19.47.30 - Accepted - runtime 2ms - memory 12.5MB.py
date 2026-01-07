"""
LeetCode: 2025 08 03 19.47.30 Accepted Runtime 2ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1): 

            oneStep = dp[i - 1] + cost[i - 1]
            twoStep = dp[i - 2] + cost[i - 2]

            dp[i] = min(oneStep, twoStep)
        
        return dp[-1]