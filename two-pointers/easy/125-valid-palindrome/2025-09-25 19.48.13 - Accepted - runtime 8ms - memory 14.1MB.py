"""
LeetCode: 2025 09 25 19.48.13 Accepted Runtime 8ms Memory 14.1mb

Algorithm:
Two-pass approach: first pass builds cleaned string with only alphanumeric characters (lowercased). Second pass compares cleaned string with its reverse. If equal, string is palindrome. This handles case-insensitive comparison and ignores non-alphanumeric characters.

Time Complexity: O(1)
Space Complexity: O(1)
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