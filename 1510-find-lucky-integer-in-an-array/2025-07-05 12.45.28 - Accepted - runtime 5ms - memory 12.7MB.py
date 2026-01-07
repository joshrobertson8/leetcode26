"""
LeetCode: 2025 07 05 12.45.28 Accepted Runtime 5ms Memory 12.7mb

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

        if luckyInt == 0:
            return -1 
        else:
            return luckyInt