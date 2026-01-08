"""
LeetCode: 2024 10 03 02.49.57 Accepted Runtime 424ms Memory 27.4MB

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
        else:
            return True