"""
LeetCode: 2024 11 09 20.11.46 Accepted Runtime 15ms Memory 11.6mb

Algorithm:
Continue while window is valid.

Time Complexity: O(n)
Space Complexity: O(1)
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