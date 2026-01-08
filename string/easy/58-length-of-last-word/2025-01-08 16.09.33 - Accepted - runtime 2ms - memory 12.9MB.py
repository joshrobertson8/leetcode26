"""
LeetCode: 2025 01 08 16.09.33 Accepted Runtime 2ms Memory 12.9mb

Algorithm:
Iterate through each index.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def lengthOfLastWord(self, s):

        count = 0 
        
        s = s.rstrip()


        for i in range(len(s)):

            if s[i] == " ":
                count = 0 
            else: 
                count += 1
        return count