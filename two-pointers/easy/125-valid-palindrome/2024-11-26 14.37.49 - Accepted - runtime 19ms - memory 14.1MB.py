"""
LeetCode: 2024 11 26 14.37.49 Accepted Runtime 19ms Memory 14.1mb

Algorithm:
TODO: Describe your approach here

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