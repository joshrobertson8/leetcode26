"""
LeetCode: 2025 12 23 16.00.45 Accepted Runtime 0ms Memory 17.2MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
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