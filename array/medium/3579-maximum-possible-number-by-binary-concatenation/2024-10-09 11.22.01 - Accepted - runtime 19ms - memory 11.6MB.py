"""
LeetCode: 2024 10 09 11.22.01 Accepted Runtime 19ms Memory 11.6mb

Problem:
import itertools

Algorithm:
Convert each number to its binary representation (without '0b' prefix). Generate all possible permutations of these binary strings. For each permutation, concatenate the binary strings and convert back to decimal. Return the maximum decimal value obtained from all permutations.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def maxGoodNumber(self, nums):
        binary_nums = [bin(n)[2:] for n in nums]
        res = max(int(''.join(p), 2) for p in itertools.permutations(binary_nums))
        return res