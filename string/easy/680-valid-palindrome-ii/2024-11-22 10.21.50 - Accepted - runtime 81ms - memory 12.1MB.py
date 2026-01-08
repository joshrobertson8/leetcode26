"""
LeetCode: 2024 11 22 10.21.50 Accepted Runtime 81ms Memory 12.1mb

Algorithm:
Two-pointer with one deletion: use left and right pointers. While characters match, move pointers inward. When mismatch found, check if palindrome can be formed by deleting either left character (check(s, left+1, right)) or right character (check(s, left, right-1)). Helper function check() verifies if substring is palindrome. Return True if original is palindrome or can become one by deleting at most one character.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def check(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check(s, left + 1, right) or check(s, left, right - 1)
            left += 1
            right -= 1
        return True