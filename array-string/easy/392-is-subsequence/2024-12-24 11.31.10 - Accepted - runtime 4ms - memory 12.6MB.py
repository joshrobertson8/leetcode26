"""
LeetCode: 2024 12 24 11.31.10 Accepted Runtime 4ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def isSubsequence(self, s, t):
        a = 0 
        b = 0 


        while a < len(s) and b < len(t):

            if s[a] == t[b]:
                a += 1
            b += 1

        return a == len(s)