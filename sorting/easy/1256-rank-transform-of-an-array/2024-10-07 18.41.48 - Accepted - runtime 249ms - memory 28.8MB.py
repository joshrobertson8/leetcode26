"""
LeetCode: 2024 10 07 18.41.48 Accepted Runtime 249ms Memory 28.8mb

Algorithm:
Sort and rank: sort array to determine order. Build ranking map: iterate through sorted array, assign rank 1 to first unique value, increment rank for each new unique value. Map each unique value to its rank (1-indexed). Then transform original array by replacing each element with its rank from the map. This assigns ranks based on sorted order, with same values getting same rank.

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