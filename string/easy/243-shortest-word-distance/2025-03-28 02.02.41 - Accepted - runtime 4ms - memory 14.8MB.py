"""
LeetCode: 2025 03 28 02.02.41 Accepted Runtime 4ms Memory 14.8mb

Algorithm:
Single pass tracking: maintain indices one and two for last positions of word1 and word2, initialized to infinity. Iterate through array: when word1 found, update one. When word2 found, update two. After each update, calculate distance abs(two - one) and track minimum. This finds shortest distance by always comparing current positions of both words.

Time Complexity: O(n)
Space Complexity: O(1)
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