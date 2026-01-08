"""
LeetCode: 2025 07 03 10.30.22 Accepted Runtime 96ms Memory 63.2mb

Algorithm:
Maintain two maps: ballToColors tracks which color each ball currently has, and uniqueColors counts how many balls have each color. For each query, if the ball already has a color, decrement the count for that color (and remove it if count becomes 0). Then assign the new color to the ball and increment its count. Append the number of distinct colors (size of uniqueColors) to the result.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        uniqueColors = {}
        ballToColors = {}
        result = []

        for ball, color in queries: 

            if ball in ballToColors:
                prevColor = ballToColors[ball]

                uniqueColors[prevColor] -= 1

                if uniqueColors[prevColor] == 0:
                    del uniqueColors[prevColor]

            ballToColors[ball] = color
            uniqueColors[color] = uniqueColors.get(color, 0) + 1
            result.append(len(uniqueColors))
            
        return result