"""
LeetCode: 2025 01 14 21.38.34 Accepted Runtime 7ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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