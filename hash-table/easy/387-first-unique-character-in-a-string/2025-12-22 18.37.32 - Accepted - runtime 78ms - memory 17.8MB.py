"""
LeetCode: 2025 12 22 18.37.32 Accepted Runtime 78ms Memory 17.8MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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