"""
LeetCode: 2025 12 23 16.00.45 Accepted Runtime 0ms Memory 17.2MB

Algorithm:
Character-by-character comparison: iterate through positions of first string. For each position i, check if all strings have same character at i. If any string is shorter (i >= len(word)) or character differs, return prefix up to i. If all positions match, return entire first string. This finds longest common prefix by comparing character by character.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0
        while i < len(strs[0]):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][0:i]

            i += 1
        return strs[0]