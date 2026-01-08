"""
LeetCode: 2024 10 23 12.29.50 Accepted Runtime 7ms Memory 11.7mb

Algorithm:
Build frequency map for string s. For each character in t, decrement its count in the map. If a character in t doesn't exist in map, return False. After processing t, check if all counts in map are zero. If any count is non-zero, return False. This verifies both strings have same characters with same frequencies.

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