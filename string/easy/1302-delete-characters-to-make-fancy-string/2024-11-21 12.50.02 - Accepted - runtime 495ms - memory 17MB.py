"""
LeetCode: 2024 11 21 12.50.02 Accepted Runtime 495ms Memory 17mb

Algorithm:
Character tracking: iterate through string, tracking consecutive character count. Start with first character in result. For each subsequent character, if it matches previous, increment count. Otherwise reset count to 1 and update previous. Only append character if count < 3 (allowing at most 2 consecutive identical characters). This removes characters that would create 3+ consecutive identical characters.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 1
        result = []
        result.append(s[0])
        
        for i in range(1, len(s)):
            
            if s[i] == s[i - 1]:
                count += 1
                if count < 3:
                    result.append(s[i])

            else:
                count = 1 
                result.append(s[i])

            
        return ''.join(result)