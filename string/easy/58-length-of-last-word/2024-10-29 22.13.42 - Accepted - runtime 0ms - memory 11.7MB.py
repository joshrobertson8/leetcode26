"""
LeetCode: 2024 10 29 22.13.42 Accepted Runtime 0ms Memory 11.7mb

Algorithm:
Reverse traversal: reverse string to process from end. Skip trailing spaces by incrementing index while character is space. Then count consecutive non-space characters until next space or end of string. Return the length. This finds the last word by working backwards.

Time Complexity: O(n)
Space Complexity: O(1)
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