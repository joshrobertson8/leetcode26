"""
LeetCode: 2024 10 02 21.24.57 Accepted Runtime 41ms Memory 11.6mb

Algorithm:
Continue until condition is met.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        standard_x = x
        reversed_x = 0

        
        while x > 0: 
            last_digit = x % 10
            reversed_x = reversed_x * 10 + last_digit
            x = x // 10
        return standard_x == reversed_x