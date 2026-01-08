"""
LeetCode: 2024 11 21 12.57.19 Accepted Runtime 8859ms Memory 16.9mb

Algorithm:
Character tracking: iterate through string, tracking consecutive character count. Start with first character in result. For each subsequent character, if it matches previous, increment count. Otherwise reset count to 1 and update previous. Only append character if count < 3 (allowing at most 2 consecutive identical characters). This removes characters that would create 3+ consecutive identical characters.

Time Complexity: O(n)
Space Complexity: O(1)
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