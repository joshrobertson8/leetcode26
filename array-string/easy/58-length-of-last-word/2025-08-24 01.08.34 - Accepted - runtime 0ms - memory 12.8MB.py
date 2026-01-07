"""
LeetCode: 2025 08 24 01.08.34 Accepted Runtime 0ms Memory 12.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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