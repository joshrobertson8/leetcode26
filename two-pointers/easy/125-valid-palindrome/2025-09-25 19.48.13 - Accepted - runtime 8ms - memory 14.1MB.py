"""
LeetCode: 2025 09 25 19.48.13 Accepted Runtime 8ms Memory 14.1mb

Algorithm:
Clean the string by removing non-alphanumeric characters, then compare with its reverse.

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