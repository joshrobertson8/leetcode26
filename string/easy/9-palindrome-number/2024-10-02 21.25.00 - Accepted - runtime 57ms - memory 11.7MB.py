"""
LeetCode: 2024 10 02 21.25.00 Accepted Runtime 57ms Memory 11.7mb

Algorithm:
Reverse number comparison: handle negative numbers (not palindromes). Reverse the number by extracting digits from right to left: repeatedly take last digit (x % 10), add to reversed number (reversed_x * 10 + last_digit), remove last digit (x // 10). Compare original number with reversed number. If equal, it's a palindrome.

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