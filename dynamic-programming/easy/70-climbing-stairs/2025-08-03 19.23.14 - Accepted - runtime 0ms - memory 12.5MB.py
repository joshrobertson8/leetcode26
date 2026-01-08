"""
LeetCode: 2025 08 03 19.23.14 Accepted Runtime 0ms Memory 12.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2: 
            return 2

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n): 

            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]