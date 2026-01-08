"""
LeetCode: 2024 10 07 18.41.48 Accepted Runtime 249ms Memory 28.8mb

Algorithm:
TODO: Describe your approach here

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
            if i not in ranking:
                ranking[i] = rank
                rank += 1
        
        for i in arr:
            result.append(ranking[i])
        return result