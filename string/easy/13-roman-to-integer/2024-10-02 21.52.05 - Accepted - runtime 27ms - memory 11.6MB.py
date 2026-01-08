"""
LeetCode: 2024 10 02 21.52.05 Accepted Runtime 27ms Memory 11.6mb

Algorithm:
Right-to-left processing: reverse string and process from right to left. Maintain prev to track previous value. For each character, get its value from roman_numerals map. If current < prev, subtract current (handles cases like IV=4, IX=9). Otherwise add current. Update prev. This correctly handles subtractive notation by processing right-to-left and subtracting when smaller value precedes larger.

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