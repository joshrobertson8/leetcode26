"""
LeetCode: 2024 11 22 10.21.50 Accepted Runtime 81ms Memory 12.1mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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