"""
LeetCode: 2024 10 29 22.13.42 Accepted Runtime 0ms Memory 11.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s[::-1]
        length = 0
        i = 0
        
        while i < len(s) and s[i] == " ":
            i += 1
            
        while i < len(s) and s[i] != " ":
            length += 1
            i += 1
        
        return length