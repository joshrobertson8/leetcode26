"""
LeetCode: 2025 10 01 20.24.14 Accepted Runtime 39ms Memory 17.3mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n log n)
Space Complexity: O(1)
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