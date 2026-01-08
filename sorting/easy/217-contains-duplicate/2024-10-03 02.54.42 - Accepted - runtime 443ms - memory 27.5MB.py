"""
LeetCode: 2024 10 03 02.54.42 Accepted Runtime 443ms Memory 27.5MB

Algorithm:
Use a set for O(1) lookup.

Time Complexity: O(1)
Space Complexity: O(n)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        unique = set(nums)
        if len(unique) == len(nums):
            return False

        return True