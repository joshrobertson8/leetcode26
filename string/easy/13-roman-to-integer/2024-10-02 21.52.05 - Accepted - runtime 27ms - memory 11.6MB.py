"""
LeetCode: 2024 10 02 21.52.05 Accepted Runtime 27ms Memory 11.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        reversed_s = s[::-1]
        result = 0
        prev = 0

        for i in reversed_s:
            current = roman_numerals[i]
            if current < prev:
                result -= current
            else:
                result += current
            prev = current
        
        return result