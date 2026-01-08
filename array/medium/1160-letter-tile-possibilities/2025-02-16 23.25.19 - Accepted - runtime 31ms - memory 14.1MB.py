"""
LeetCode: 2025 02 16 23.25.19 Accepted Runtime 31ms Memory 14.1mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

Time Complexity: O(n²)
Space Complexity: O(n)
"""

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        hashset = set()

        for i in range(1, len(tiles) + 1):
            for j in permutations(tiles, i):
                hashset.add(j)
        
        return len(hashset)