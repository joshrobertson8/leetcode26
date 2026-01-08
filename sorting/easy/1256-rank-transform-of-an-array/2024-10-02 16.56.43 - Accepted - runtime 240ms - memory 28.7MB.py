"""
LeetCode: 2024 10 02 16.56.43 Accepted Runtime 240ms Memory 28.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def arrayRankTransform(self, arr):

        ranking = {}
        rank = 1
        sorted_arr = sorted(arr)

        for i in sorted_arr:
            if i not in ranking:
                ranking[i] = rank
                rank += 1
        return [ranking[rank] for rank in arr]