"""
LeetCode: 2024 11 05 00.27.46 Accepted Runtime 0ms Memory 11.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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