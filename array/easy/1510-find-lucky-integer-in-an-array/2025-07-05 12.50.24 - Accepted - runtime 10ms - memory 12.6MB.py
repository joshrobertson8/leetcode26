"""
LeetCode: 2025 07 05 12.50.24 Accepted Runtime 10ms Memory 12.6mb

Algorithm:
Use Counter to build a frequency map. Then iterate through the array: for each number, check if its frequency equals the number itself (a lucky number). Use max to track the maximum lucky number found. Return -1 if no lucky number exists, otherwise return the maximum.

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
            if num in freqMap:
                if num == freqMap[num]:
                    luckyInt = max(luckyInt, num)

        return luckyInt if luckyInt != 0 else -1