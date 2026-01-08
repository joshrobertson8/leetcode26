"""
LeetCode: 2025 07 05 12.45.28 Accepted Runtime 5ms Memory 12.7mb

Algorithm:
First pass: build a frequency map counting occurrences of each number. Second pass: for each number in the array, check if its frequency equals the number itself (a lucky number). Track the maximum lucky number found. Return -1 if no lucky number exists, otherwise return the maximum.

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

        if luckyInt == 0:
            return -1 
        else:
            return luckyInt