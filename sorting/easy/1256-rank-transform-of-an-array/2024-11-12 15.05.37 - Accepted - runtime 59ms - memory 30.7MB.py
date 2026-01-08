"""
LeetCode: 2024 11 12 15.05.37 Accepted Runtime 59ms Memory 30.7mb

Algorithm:
Sort and rank: sort array to determine order. Build ranking map: iterate through sorted array, increment rank when encountering a new (larger) value. Map each unique value to its rank (1-indexed). Then transform original array by replacing each element with its rank from the map. This assigns ranks based on sorted order, with same values getting same rank.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def arrayRankTransform(self, arr):

        ranking = {}
        sortedarr = sorted(arr) 
        rank = 1
        for i in range(len(sortedarr)):
            if sortedarr[i] > sortedarr[i - 1]:
                rank += 1
            ranking[sortedarr[i]] = rank
        for i in range(len(arr)):
            arr[i] = ranking[arr[i]]

        return arr