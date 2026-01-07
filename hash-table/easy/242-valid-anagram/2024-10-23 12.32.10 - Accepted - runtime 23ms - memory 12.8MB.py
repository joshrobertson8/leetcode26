"""
LeetCode: 2024 10 23 12.32.10 Accepted Runtime 23ms Memory 12.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def isAnagram(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s != sorted_t:
            return False
        return True