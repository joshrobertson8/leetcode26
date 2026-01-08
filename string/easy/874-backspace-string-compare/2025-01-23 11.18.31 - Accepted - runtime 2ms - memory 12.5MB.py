"""
LeetCode: 2025 01 23 11.18.31 Accepted Runtime 2ms Memory 12.5mb

Algorithm:
Stack-based approach.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def helper(word):

            result = []
            for char in word:
                if char != "#":
                    result.append(char)
                else:
                    if result:
                        result.pop()
            return result

        
        return helper(s) == helper(t)