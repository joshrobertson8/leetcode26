"""
LeetCode: 2025 07 03 08.53.36 Accepted Runtime 25ms Memory 12.4mb

Algorithm:
Iterate through the array once.

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