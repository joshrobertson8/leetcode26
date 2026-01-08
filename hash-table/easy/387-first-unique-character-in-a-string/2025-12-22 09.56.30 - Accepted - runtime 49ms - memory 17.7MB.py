"""
LeetCode: 2025 12 22 09.56.30 Accepted Runtime 49ms Memory 17.7MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for idx, val in enumerate(s):

            if counter[val] == 1: 
                return idx
        return -1