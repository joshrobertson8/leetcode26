"""
LeetCode: 2024 10 07 17.22.18 Accepted Runtime 20ms Memory 11.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def strStr(self, haystack, needle):

        n = len(needle)
        m = len(haystack)
    
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        
        return -1