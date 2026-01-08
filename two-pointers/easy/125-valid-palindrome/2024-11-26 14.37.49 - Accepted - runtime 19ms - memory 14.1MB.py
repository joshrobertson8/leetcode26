"""
LeetCode: 2024 11 26 14.37.49 Accepted Runtime 19ms Memory 14.1mb

Algorithm:
Two-pass two pointers: first pass builds cleaned string with only alphanumeric characters (lowercased). Second pass uses two pointers (L, R) comparing characters from both ends. If characters differ, return False. If all match, return True. This handles case-insensitive comparison and ignores non-alphanumeric characters.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        L = 0 
        R = len(cleaned) - 1

        while L < R:

            if cleaned[L] != cleaned[R]:
                return False

            R -= 1
            L += 1

        return True