"""
LeetCode: 2025 07 05 12.47.09 Accepted Runtime 3ms Memory 12.6mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

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

        freqMap = {}

        for i in range(len(arr)):

            if arr[i] in freqMap:
                freqMap[arr[i]] += 1
            else:
                freqMap[arr[i]] = 1

        for num in arr:

            if num in freqMap and freqMap[num] == num:
                if num > luckyInt:
                    luckyInt = num

        return luckyInt if luckyInt != 0 else -1