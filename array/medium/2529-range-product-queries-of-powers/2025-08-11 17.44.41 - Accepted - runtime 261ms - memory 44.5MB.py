"""
LeetCode: 2025 08 11 17.44.41 Accepted Runtime 261ms Memory 44.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
Space Complexity: O(n)
"""

class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7

        # build powers (ascending)
        powers = []
        bit = 1
        while n != 0:
            if n & 1:
                powers.append(bit)
            bit *= 2
            n >>= 1

        res = []

        for l, r in queries:
            product = 1

            for i in range(l, r + 1): 
                product = (product * powers[i]) % MOD
            res.append(product)

        return res