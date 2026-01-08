"""
LeetCode: 2024 11 04 20.32.04 Accepted Runtime 3ms Memory 11.6mb

Algorithm:
Build prefix array.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        i = 0 
        while i < len(strs[0]):
            for j in strs:
                if i >= len(j) or j[i] != strs[0][i]:
                    return strs[0][0:i]
            i += 1
        return strs[0]