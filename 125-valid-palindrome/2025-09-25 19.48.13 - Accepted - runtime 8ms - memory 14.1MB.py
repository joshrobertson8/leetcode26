"""
LeetCode: 2025 09 25 19.48.13 Accepted Runtime 8ms Memory 14.1mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        reversedClean = cleaned[::-1]

        return cleaned == reversedClean