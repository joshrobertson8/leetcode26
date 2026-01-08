"""
LeetCode: 2024 10 23 12.25.01 Accepted Runtime 9ms Memory 11.8mb

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
        
        return all(i == 0 for i in hashmap.values())