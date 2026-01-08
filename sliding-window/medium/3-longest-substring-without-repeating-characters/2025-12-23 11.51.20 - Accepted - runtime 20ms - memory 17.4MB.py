"""
LeetCode: 2025 12 23 11.51.20 Accepted Runtime 20ms Memory 17.4MB

Algorithm:
Sliding window with set: use left (l) and right (r) pointers. For each character at r, if it's already in seen set, shrink window from left (remove s[l] from set, increment l) until s[r] is not in seen. Add s[r] to set and update maximum length (r - l + 1). This finds longest substring without repeating characters.

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