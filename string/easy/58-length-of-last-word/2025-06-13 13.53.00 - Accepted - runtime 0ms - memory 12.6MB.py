"""
LeetCode: 2025 06 13 13.53.00 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def lengthOfLastWord(self, s):

        clean = s.strip()
        count = 0 

        for char in clean:

            if char == " ":
                count = 0

            else:
                count += 1

        return count