"""
LeetCode: 2025 12 22 09.56.30 Accepted Runtime 49ms Memory 17.7MB

Algorithm:
Use Counter to count character frequencies. Then iterate through string with enumerate. Return the index of the first character with frequency 1. If no unique character found, return -1.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for idx, val in enumerate(s):

            if counter[val] == 1: 
                return idx
        return -1