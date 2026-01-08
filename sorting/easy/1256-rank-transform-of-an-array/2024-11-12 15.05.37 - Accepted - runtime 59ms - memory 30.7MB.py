"""
LeetCode: 2024 11 12 15.05.37 Accepted Runtime 59ms Memory 30.7mb

Algorithm:
TODO: Describe your approach here

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