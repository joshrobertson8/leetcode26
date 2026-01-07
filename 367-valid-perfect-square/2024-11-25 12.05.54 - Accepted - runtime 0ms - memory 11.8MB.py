"""
LeetCode: 2024 11 25 12.05.54 Accepted Runtime 0ms Memory 11.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1
        high = num 

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if num == square:
                return True 

            elif square > num:
                high = mid - 1
        
            else:
                low = mid + 1

        return False