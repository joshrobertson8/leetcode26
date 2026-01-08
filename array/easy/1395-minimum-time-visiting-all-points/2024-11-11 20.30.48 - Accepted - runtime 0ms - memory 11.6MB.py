"""
LeetCode: 2024 11 11 20.30.48 Accepted Runtime 0ms Memory 11.6mb

Algorithm:
TODO: Describe your approach here

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