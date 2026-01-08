"""
LeetCode: 2025 01 28 23.40.44 Accepted Runtime 1ms Memory 12.3mb

Algorithm:
Two-pointer matching: use pointer a for s and c for length of s. Use pointer b for t. While both pointers valid, if s[a] == t[b], advance a (found character from s). Always advance b. After loop, if a == c, all characters of s were found in order in t (subsequence exists). This checks if s is subsequence of t by matching characters in order.

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