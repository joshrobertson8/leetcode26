"""
LeetCode: 2024 10 09 11.22.01 Accepted Runtime 19ms Memory 11.6mb

Problem:
import itertools

Algorithm:
TODO: Describe your approach here

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxGoodNumber(self, nums):
        binary_nums = [bin(n)[2:] for n in nums]
        res = max(int(''.join(p), 2) for p in itertools.permutations(binary_nums))
        return res