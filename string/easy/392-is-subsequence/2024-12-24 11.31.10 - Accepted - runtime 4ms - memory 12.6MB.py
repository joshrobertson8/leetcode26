"""
LeetCode: 2024 12 24 11.31.10 Accepted Runtime 4ms Memory 12.6mb

Algorithm:
Two-pointer matching: use pointer a for s and b for t. While both pointers valid, if s[a] == t[b], advance a (found character from s). Always advance b. After loop, if a == len(s), all characters of s were found in order in t (subsequence exists). This checks if s is subsequence of t by matching characters in order.

Time Complexity: O(n)
Space Complexity: O(1)
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