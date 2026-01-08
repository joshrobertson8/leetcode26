"""
LeetCode: 2024 11 20 13.12.57 Accepted Runtime 5ms Memory 11.6mb

Algorithm:
Use set to detect cycles. Helper function computes sum of squares of digits. While output != 1 and not seen before, add to set and compute next number. If we reach 1, return True. If we see a number again (cycle), return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isHappy(self, n):
        output = n

        def get_next_number(output):
            output = sum(int(digit) ** 2 for digit in str(output))
            return output

        seen = set()

        while output != 1 and output not in seen:
            seen.add(output)
            output = get_next_number(output)

        return output == 1