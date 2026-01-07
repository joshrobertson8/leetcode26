"""
LeetCode: 2024 11 21 12.57.19 Accepted Runtime 8859ms Memory 16.9mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s[0]
        count = 1
        prev = s[0]

        for i in range(1, len(s)):

            if s[i] == prev:
                count += 1
            else:
                count = 1
                prev = s[i]
            if count < 3:
                result += s[i]

        return result