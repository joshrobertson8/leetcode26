"""
LeetCode: 2024 10 02 21.04.09 Accepted Runtime 19ms Memory 11.6mb

Algorithm:
String reversal comparison: convert number to string. Reverse string using slice notation [::-1]. Compare reversed string with original. If equal, number is palindrome. Simple approach using string operations.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, x):
        isPalindrome = True

        x = str(x)

        reversed_x = x[::-1]

        if reversed_x != x:
            isPalindrome = False
        
        return isPalindrome