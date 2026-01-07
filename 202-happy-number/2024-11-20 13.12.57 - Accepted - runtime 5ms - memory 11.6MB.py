"""
LeetCode: 2024 11 20 13.12.57 Accepted Runtime 5ms Memory 11.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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