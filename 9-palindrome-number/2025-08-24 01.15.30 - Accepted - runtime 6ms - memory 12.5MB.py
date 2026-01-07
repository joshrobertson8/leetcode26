"""
LeetCode: 2025 08 24 01.15.30 Accepted Runtime 6ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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