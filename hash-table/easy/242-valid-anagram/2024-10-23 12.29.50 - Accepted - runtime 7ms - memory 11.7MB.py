"""
LeetCode: 2024 10 23 12.29.50 Accepted Runtime 7ms Memory 11.7mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isAnagram(self, s, t):
        hashmap = {}

        for i in s:
            
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for i in t:
            if i in hashmap:
                hashmap[i] -= 1
            else:
                return False

        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True