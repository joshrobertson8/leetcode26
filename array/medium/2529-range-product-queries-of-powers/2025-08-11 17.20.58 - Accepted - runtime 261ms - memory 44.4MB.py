"""
LeetCode: 2025 08 11 17.20.58 Accepted Runtime 261ms Memory 44.4mb

Algorithm:
First, decompose n into powers of 2 by checking each bit: if bit i is set, add 2^i to the powers list. Then for each query [l, r], compute the product of powers[l] through powers[r], applying modulo 10^9+7 at each multiplication step to prevent overflow. Return the list of products.

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

        # answer queries by multiplying powers directly (mod as you go)
        ans = []
        for l, r in queries:
            prod = 1
            for i in range(l, r + 1):
                prod = (prod * powers[i]) % MOD
            ans.append(prod)
        return ans