"""
LeetCode: 2025 01 28 23.40.44 Accepted Runtime 1ms Memory 12.3mb

Algorithm:
Nested loops to check all pairs.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def isSubsequence(self, s, t):
        a = 0  # Pointer for s
        b = 0  # Pointer for t
        c = len(s)

        while a < c and b < len(t):
            if s[a] == t[b]:
                a += 1
            b += 1

        return a == c