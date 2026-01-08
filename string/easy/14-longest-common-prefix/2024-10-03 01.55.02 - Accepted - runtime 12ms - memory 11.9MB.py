"""
LeetCode: 2024 10 03 01.55.02 Accepted Runtime 12ms Memory 11.9mb

Algorithm:
Character-by-character comparison: iterate through positions of first string. For each position i, check if all strings have same character at i. If any string is shorter (i >= len(j)) or character differs (j[i] != strs[0][i]), return prefix up to i. If all positions match, return entire first string. This finds longest common prefix by comparing character by character.

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