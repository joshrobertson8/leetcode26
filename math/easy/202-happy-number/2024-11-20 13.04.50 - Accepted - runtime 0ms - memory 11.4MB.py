"""
LeetCode: 2024 11 20 13.04.50 Accepted Runtime 0ms Memory 11.4mb

Algorithm:
Use set to detect cycles. Helper function computes sum of squares of digits. While output != 1 and not seen before, add to set and compute next number. If we reach 1, return True. If we see a number again (cycle), return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isHappy(self, n):
        output = n

        def get_next_number(num):
            next_num = sum(int(digit) ** 2 for digit in str(num))
            return next_num

        seen = set()

        while output != 1 and output not in seen:
            seen.add(output)
            output = get_next_number(output)

        return output == 1