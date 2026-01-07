"""
LeetCode: 2024 10 03 02.54.45 Accepted Runtime 426ms Memory 27.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        unique = set(nums)
        if len(unique) == len(nums):
            return False

        return True