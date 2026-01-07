"""
LeetCode: 2025 07 05 12.50.24 Accepted Runtime 10ms Memory 12.6mb

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
            if num in freqMap:
                if num == freqMap[num]:
                    luckyInt = max(luckyInt, num)

        return luckyInt if luckyInt != 0 else -1