"""
LeetCode: 2025 03 28 02.00.37 Accepted Runtime 4ms Memory 14.7mb

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
        res = float('inf') 

        for i in range(len(wordsDict)):

            if wordsDict[i] == word1:
                one = i

            elif wordsDict[i] == word2:
                two = i

            res = min(res, abs(two - one))

        return res