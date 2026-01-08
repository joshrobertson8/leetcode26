"""
LeetCode: 2024 10 23 12.32.10 Accepted Runtime 23ms Memory 12.8mb

Algorithm:
Sort both strings and compare them. If sorted strings are equal, they are anagrams (same characters in different order). Return True if sorted_s == sorted_t, False otherwise. This is simpler but less efficient due to sorting.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution(object):
    def isAnagram(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s != sorted_t:
            return False
        return True