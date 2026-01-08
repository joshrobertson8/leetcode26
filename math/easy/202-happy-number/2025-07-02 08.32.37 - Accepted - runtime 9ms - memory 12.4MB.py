"""
LeetCode: 2025 07 02 08.32.37 Accepted Runtime 9ms Memory 12.4mb

Algorithm:
Use set to detect cycles. Helper function computes sum of squares of digits. While val != 1, if val is in seen (cycle detected), return False. Otherwise add to set and compute next number. If we reach 1, return True.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        val = n

        
        
        def operation(val):
            total = 0

            for num in str(val):

                total += int(num) ** 2

            return total

        
        while val != 1:

            if val in seen:
                return False
            seen.add(val)
            val = operation(val)

        return True