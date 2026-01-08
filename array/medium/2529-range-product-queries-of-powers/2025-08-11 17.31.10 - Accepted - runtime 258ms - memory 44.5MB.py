"""
LeetCode: 2025 08 11 17.31.10 Accepted Runtime 258ms Memory 44.5mb

Algorithm:
Use nested loops to check all pairs.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7

        # build powers (ascending)
        powers = []
        bit = 1
        x = n
        while x != 0:
            if x & 1:
                powers.append(bit)
            bit *= 2
            x >>= 1

        res = []

        for l, r in queries:
            product = 1

            for i in range(l, r + 1): 
                product = (product * powers[i]) % MOD
            res.append(product)

        return res