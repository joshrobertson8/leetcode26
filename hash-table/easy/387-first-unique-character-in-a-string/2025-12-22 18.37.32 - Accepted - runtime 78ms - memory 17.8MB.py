"""
LeetCode: 2025 12 22 18.37.32 Accepted Runtime 78ms Memory 17.8MB

Algorithm:
Build frequency map counting character occurrences. Then iterate through string with enumerate. Return the index of the first character with frequency 1. If no unique character found, return -1.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}

        for ch in s: 
            if ch in counts: 
                counts[ch] += 1
            else: 
                counts[ch] = 1

        for idx, val in enumerate(s): 

            if counts[val] == 1: 
                return idx
            
        return -1