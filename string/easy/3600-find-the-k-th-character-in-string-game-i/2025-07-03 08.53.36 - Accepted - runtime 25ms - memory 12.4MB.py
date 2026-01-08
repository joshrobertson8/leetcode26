"""
LeetCode: 2025 07 03 08.53.36 Accepted Runtime 25ms Memory 12.4mb

Algorithm:
String expansion: start with word = "a". While word length < k, expand by appending transformed version: for each character in current word, if 'z', append 'a', otherwise append next character (chr(ord(char) + 1)). Continue expanding until word length >= k. Return character at index k-1. This simulates string game where each iteration appends incremented version of current string.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"

        while len(word) < k:

            result = ""

            for char in word:

                if char == 'z':
                    result += 'a'
                else:
                    result += chr(ord(char) + 1)
                
            word += result

        return word[k - 1]