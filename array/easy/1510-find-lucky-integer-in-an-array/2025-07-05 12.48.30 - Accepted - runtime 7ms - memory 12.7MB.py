"""
LeetCode: 2025 07 05 12.48.30 Accepted Runtime 7ms Memory 12.7mb

Algorithm:
Use Counter to build a frequency map. Then iterate through the array: for each number, check if its frequency equals the number itself (a lucky number). Track the maximum lucky number found. Return -1 if no lucky number exists, otherwise return the maximum.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        luckyInt = 0

        freqMap = Counter(arr)

        for num in arr:
            if num in freqMap and freqMap[num] == num:
                if num > luckyInt:
                    luckyInt = num

        return luckyInt if luckyInt != 0 else -1