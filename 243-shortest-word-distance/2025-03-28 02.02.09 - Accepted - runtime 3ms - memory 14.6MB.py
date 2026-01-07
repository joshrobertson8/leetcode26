"""
LeetCode: 2025 03 28 02.02.09 Accepted Runtime 3ms Memory 14.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        one = float('inf')
        two = float('inf')
        res = 100000000

        for i in range(len(wordsDict)):

            if wordsDict[i] == word1:
                one = i

            elif wordsDict[i] == word2:
                two = i

            res = min(res, abs(two - one))

        return res