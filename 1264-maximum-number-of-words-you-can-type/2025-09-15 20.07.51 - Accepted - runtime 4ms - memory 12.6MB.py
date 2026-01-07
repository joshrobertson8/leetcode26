"""
LeetCode: 2025 09 15 20.07.51 Accepted Runtime 4ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        seen = set(brokenLetters)
        words = text.split(" ")
        count = 0 

        for word in words: 
            for char in word:
                if char in seen:
                    count +=1
                    break
                    
        return len(words) - count