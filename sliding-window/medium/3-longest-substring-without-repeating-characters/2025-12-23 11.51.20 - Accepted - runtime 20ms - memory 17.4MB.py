"""
LeetCode: 2025 12 23 11.51.20 Accepted Runtime 20ms Memory 17.4MB

Algorithm:
Use a hash table to store seen elements for O(1) lookup. Greedy algorithm.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen = set()

        for r in range(len(s)):

            while s[r] in seen: 
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            res = max(res, r - l + 1)
        return res