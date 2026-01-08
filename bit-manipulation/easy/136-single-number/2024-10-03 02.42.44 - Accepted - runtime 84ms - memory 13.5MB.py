"""
LeetCode: 2024 10 03 02.42.44 Accepted Runtime 84ms Memory 13.5mb

Algorithm:
Use XOR bitwise operation: XOR of a number with itself is 0, and XOR with 0 is the number itself. Since all numbers appear twice except one, XORing all numbers cancels out the pairs, leaving only the single number. Initialize result to 0, then XOR each number in the array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result