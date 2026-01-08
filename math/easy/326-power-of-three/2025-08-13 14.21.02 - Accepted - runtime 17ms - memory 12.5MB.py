"""
LeetCode: 2025 08 13 14.21.02 Accepted Runtime 17ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 3 == 0:

            n /= 3

        return n == 1