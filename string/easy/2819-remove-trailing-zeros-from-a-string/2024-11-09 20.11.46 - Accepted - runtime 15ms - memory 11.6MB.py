"""
LeetCode: 2024 11 09 20.11.46 Accepted Runtime 15ms Memory 11.6mb

Algorithm:
Backward traversal: start from end of string (i = len(num) - 1). While i >= 0 and character at i is '0', decrement i. Return substring from start to i+1 (num[:i+1]). This removes all trailing zeros by finding the last non-zero character from the end.

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