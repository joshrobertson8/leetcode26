"""
LeetCode: 2025 07 11 13.35.06 Accepted Runtime 0ms Memory 13mb

Algorithm:
Iterate through nums.

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