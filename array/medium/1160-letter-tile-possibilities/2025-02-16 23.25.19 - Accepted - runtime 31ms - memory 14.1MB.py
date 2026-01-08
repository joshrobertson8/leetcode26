"""
LeetCode: 2025 02 16 23.25.19 Accepted Runtime 31ms Memory 14.1mb

Algorithm:
Generate all possible permutations of tiles for lengths from 1 to len(tiles). Use itertools.permutations to generate each permutation. Store all unique permutations in a set to avoid duplicates. Return the size of the set, which represents the number of distinct tile sequences possible.

Time Complexity: O(n^2)
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