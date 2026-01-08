"""
LeetCode: 2024 10 30 09.38.20 Accepted Runtime 982ms Memory 12.9mb

Algorithm:
Two-pass approach: first pass builds cleaned string with only alphanumeric characters (lowercased). Second pass compares cleaned string with its reverse. If equal, string is palindrome. This handles case-insensitive comparison and ignores non-alphanumeric characters.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parced_s = ""
        
        for char in s:
            if char.isalnum():
                parced_s += char.lower()

        reversed_s = parced_s[::-1]

        return reversed_s == parced_s