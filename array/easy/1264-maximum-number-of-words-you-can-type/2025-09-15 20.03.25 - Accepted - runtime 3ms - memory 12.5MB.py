"""
LeetCode: 2025 09 15 20.03.25 Accepted Runtime 3ms Memory 12.5mb

Algorithm:
Convert brokenLetters to a set for O(1) lookup. Split the text into words. For each word, check if any character is in the broken set. If found, increment the count of untypeable words. Return the total words minus untypeable words.

Time Complexity: O(n^2)
Space Complexity: O(n)
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