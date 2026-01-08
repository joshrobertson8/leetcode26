"""
LeetCode: 2024 11 20 13.04.50 Accepted Runtime 0ms Memory 11.4mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

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