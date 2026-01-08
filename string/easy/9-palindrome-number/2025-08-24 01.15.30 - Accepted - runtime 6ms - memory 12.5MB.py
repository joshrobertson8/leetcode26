"""
LeetCode: 2025 08 24 01.15.30 Accepted Runtime 6ms Memory 12.5mb

Algorithm:
Process the input directly.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        
        return  str(x) == "".join(reversed(str(x)))