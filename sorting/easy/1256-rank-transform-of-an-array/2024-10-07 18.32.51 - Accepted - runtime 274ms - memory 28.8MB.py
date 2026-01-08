"""
LeetCode: 2024 10 07 18.32.51 Accepted Runtime 274ms Memory 28.8mb

Algorithm:
Sort the input first.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def arrayRankTransform(self, arr):

        ranking = {}
        sorted_arr = sorted(arr)
        result = []

        rank = 1
        for i in sorted_arr:
            if i not in ranking:  # Only assign rank if the value isn't already ranked
                ranking[i] = rank
                rank += 1

        # Build the result by mapping original arr values to their ranks
        for num in arr:
            result.append(ranking[num])

        return result