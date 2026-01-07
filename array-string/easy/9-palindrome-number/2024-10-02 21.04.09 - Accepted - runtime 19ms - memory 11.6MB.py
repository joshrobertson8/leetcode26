"""
LeetCode: 2024 10 02 21.04.09 Accepted Runtime 19ms Memory 11.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def isPalindrome(self, x):
        isPalindrome = True

        x = str(x)

        reversed_x = x[::-1]

        if reversed_x != x:
            isPalindrome = False
        
        return isPalindrome