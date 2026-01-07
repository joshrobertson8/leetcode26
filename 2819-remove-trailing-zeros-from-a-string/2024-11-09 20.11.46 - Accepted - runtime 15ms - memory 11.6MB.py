"""
LeetCode: 2024 11 09 20.11.46 Accepted Runtime 15ms Memory 11.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        i = len(num) - 1

        while i >= 0 and num[i] == '0':
            i -= 1

        return num[:i + 1]