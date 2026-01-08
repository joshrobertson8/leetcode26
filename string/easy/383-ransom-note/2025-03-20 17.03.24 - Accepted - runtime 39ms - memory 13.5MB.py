"""
LeetCode: 2025 03 20 17.03.24 Accepted Runtime 39ms Memory 13.5mb

Algorithm:
Character frequency counting: build frequency map of characters in magazine. Then iterate through ransomNote: for each character, check if it exists in map with count > 0. If not found or count is 0, cannot construct ransom note, return False. Otherwise decrement count. If all characters can be used, return True. This checks if magazine contains enough of each character needed for ransom note.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = {}
        
        for i in range(len(magazine)):
            
            if magazine[i] in hashmap:
                hashmap[magazine[i]] += 1
            else:
                hashmap[magazine[i]] = 1

        for i in range(len(ransomNote)):

            if ransomNote[i] not in hashmap or hashmap[ ransomNote[i]] == 0:
                return False
            else:
                hashmap[ransomNote[i]] -= 1
        return True