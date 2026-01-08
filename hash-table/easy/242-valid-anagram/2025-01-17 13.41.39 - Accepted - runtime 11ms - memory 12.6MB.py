"""
LeetCode: 2025 01 17 13.41.39 Accepted Runtime 11ms Memory 12.6mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        hashm = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        
        for char in t:
            if char in hashm:
                hashm[char] += 1
            else:
                hashm[char] = 1

        return hashmap == hashm