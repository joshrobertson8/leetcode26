"""
LeetCode: 2025 07 11 13.35.06 Accepted Runtime 0ms Memory 13mb

Algorithm:
Two-pass approach: first pass collects all even numbers into evens list, second pass collects all odd numbers into odds list. Return evens + odds. This separates evens and odds, placing evens first, then odds. O(n) time but requires extra space.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = []
        odds = []

        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        return evens + odds