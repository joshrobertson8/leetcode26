"""
LeetCode: 2024 10 23 12.32.10 Accepted Runtime 23ms Memory 12.8mb

Algorithm:
Sort the array first.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def isAnagram(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s != sorted_t:
            return False
        return True