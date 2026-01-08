"""
LeetCode: 2025 08 08 11.10.30 Accepted Runtime 18ms Memory 14.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """

        units = (n + 24) // 25 
        if n >= 4800:
            return 1.0


        memo = {} 

        def dfs(soupA, soupB):

            if soupA <= 0 and soupB <= 0:
                return 0.5

            if soupA <= 0:
                return 1.0

            if soupB <= 0:
                return 0.0

            if (soupA, soupB) in memo: 
                return memo[(soupA, soupB)]
            
            result =  0.25 * (
                dfs(soupA - 4.0, soupB) +
                dfs(soupA - 3.0, soupB - 1.0) +
                dfs(soupA - 2.0, soupB - 2.0) +
                dfs(soupA - 1.0, soupB - 3.0)
            )

            memo[(soupA, soupB)] = result
            return result

        return dfs(units, units)