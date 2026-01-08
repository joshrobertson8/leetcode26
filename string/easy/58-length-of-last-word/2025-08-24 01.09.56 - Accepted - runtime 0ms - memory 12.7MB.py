"""
LeetCode: 2025 08 24 01.09.56 Accepted Runtime 0ms Memory 12.7mb

Algorithm:
Iterate backwards through the array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        clean = s.strip()
        count = 0 

        for i in range(len(clean) - 1, -1, -1):

            if clean[i] != " ":
                count += 1
            
            else:
                return count 
        return count