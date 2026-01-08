"""
LeetCode: 2024 11 05 00.27.46 Accepted Runtime 0ms Memory 11.7mb

Algorithm:
Start from the rightmost digit and work backwards. If a digit is 9, set it to 0 and continue (carry over). If it's not 9, increment it and return immediately. If we finish the loop (all digits were 9), prepend 1 to the array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)

        
        for i in range(length):

            idx = length - 1 - i 

            if digits[idx] == 9:
                digits[idx] = 0

            else:
                digits[idx] += 1
            
                return digits
        return [1] + digits