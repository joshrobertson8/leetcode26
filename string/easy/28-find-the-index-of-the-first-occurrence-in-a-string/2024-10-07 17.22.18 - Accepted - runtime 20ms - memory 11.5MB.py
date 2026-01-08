"""
LeetCode: 2024 10 07 17.22.18 Accepted Runtime 20ms Memory 11.5mb

Algorithm:
Iterate through each index.

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