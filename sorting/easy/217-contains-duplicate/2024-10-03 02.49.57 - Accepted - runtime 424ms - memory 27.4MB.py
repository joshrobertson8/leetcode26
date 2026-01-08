"""
LeetCode: 2024 10 03 02.49.57 Accepted Runtime 424ms Memory 27.4MB

Algorithm:
Convert array to set to remove duplicates. If set length equals array length, no duplicates exist (return False). Otherwise, duplicates exist (return True). This leverages set's automatic duplicate removal property.

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