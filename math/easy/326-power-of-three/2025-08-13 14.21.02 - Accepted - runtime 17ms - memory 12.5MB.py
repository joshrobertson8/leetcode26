"""
LeetCode: 2025 08 13 14.21.02 Accepted Runtime 17ms Memory 12.5mb

Algorithm:
Handle non-positive numbers (return False). Repeatedly divide n by 3 while n % 3 == 0. If final result is 1, n is a power of three. Otherwise, it's not. This checks if n can be reduced to 1 by repeated division by 3.

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