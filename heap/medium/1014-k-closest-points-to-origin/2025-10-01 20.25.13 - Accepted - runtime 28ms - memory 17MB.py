"""
LeetCode: 2025 10 01 20.25.13 Accepted Runtime 28ms Memory 17mb

Algorithm:
Define distance formula (x^2 + y^2, no sqrt needed for comparison). Sort points by distance. Return first k points. This is simpler than heap but O(n log n) vs O(n log k) with heap.

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