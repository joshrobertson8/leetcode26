"""
LeetCode: 2024 10 30 09.38.44 Accepted Runtime 1027ms Memory 13mb

Algorithm:
Clean the string by removing non-alphanumeric characters, then compare with its reverse.

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