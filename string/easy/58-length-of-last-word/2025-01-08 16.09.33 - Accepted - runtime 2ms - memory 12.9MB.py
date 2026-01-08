"""
LeetCode: 2025 01 08 16.09.33 Accepted Runtime 2ms Memory 12.9mb

Algorithm:
Character counting with reset: strip trailing spaces. Iterate through string: if character is space, reset count to 0. Otherwise increment count. After iteration, count holds length of last word (since spaces reset count, final count is last word's length). This finds last word length by counting characters and resetting on spaces.

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