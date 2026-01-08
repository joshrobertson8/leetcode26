"""
LeetCode: 2024 11 11 20.30.48 Accepted Runtime 0ms Memory 11.6mb

Algorithm:
To move from one point to another in 8-directional movement (including diagonals), the time needed is the maximum of the horizontal and vertical distances. This is because we can move diagonally to cover both dimensions simultaneously. Sum up the time needed to move between consecutive points.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        for i in range(1, len(points)):
            # Calculate the difference in x and y coordinates
            dx = abs(points[i][0] - points[i - 1][0])
            dy = abs(points[i][1] - points[i - 1][1])
            # Add the max of dx and dy to time
            time += max(dx, dy)
        
        return time