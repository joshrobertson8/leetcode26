"""
LeetCode: 2024 10 03 01.54.22 Accepted Runtime 20ms Memory 11.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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