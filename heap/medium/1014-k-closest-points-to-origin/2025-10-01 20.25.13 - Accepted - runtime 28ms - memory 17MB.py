"""
LeetCode: 2025 10 01 20.25.13 Accepted Runtime 28ms Memory 17mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def distanceFormula(point): 
            return point[0] ** 2 + point[1] ** 2
        
        points.sort(key=distanceFormula)

        return points[:k]