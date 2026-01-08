"""
LeetCode: 2024 10 07 17.22.18 Accepted Runtime 20ms Memory 11.5mb

Algorithm:
Brute force string matching: for each starting position i in haystack (0 to len(haystack) - len(needle)), check if needle matches substring starting at i using slice comparison. If match found (haystack[i:i+n] == needle), return i. If no match found after checking all positions, return -1. This finds first occurrence of needle in haystack.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def strStr(self, haystack, needle):

        n = len(needle)
        m = len(haystack)
    
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        
        return -1