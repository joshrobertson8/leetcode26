"""
LeetCode: 2025 01 14 21.38.34 Accepted Runtime 7ms Memory 12.5mb

Algorithm:
Reverse and rebuild: reverse entire string first. Then iterate through reversed string, building words character by character. When space encountered and word exists, reverse the word (to restore original order) and add to result list, then clear word. After iteration, add final word if exists. Join words with spaces. This reverses word order while keeping characters within each word in original order.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s = s[::-1]
        word = ""
        result = [] 

        for char in reversed_s:

            if char != " ":
                word += char

            else:
                if word:
                    result.append(word[::-1])
                    word = ""

        if word:
            result.append(word[::-1])
        
        return " ".join(result)