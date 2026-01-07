"""
LeetCode: 2025 07 05 12.48.30 Accepted Runtime 7ms Memory 12.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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