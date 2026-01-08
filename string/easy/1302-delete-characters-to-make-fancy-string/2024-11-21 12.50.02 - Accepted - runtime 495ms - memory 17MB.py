"""
LeetCode: 2024 11 21 12.50.02 Accepted Runtime 495ms Memory 17mb

Algorithm:
TODO: Describe your approach here

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