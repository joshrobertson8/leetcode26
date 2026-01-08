"""
LeetCode: 2025 09 27 19.27.07 Accepted Runtime 12ms Memory 17mb

Algorithm:
Sort intervals by start time. Initialize result with first interval. For each subsequent interval, if it overlaps with last interval in result (res[-1][1] >= start), merge by updating end to max of both ends. Otherwise, append as new interval. This merges all overlapping intervals.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]


        for start, end in intervals[1:]:

            if res[-1][1] >= start: 
                res[-1][1] = max(end, res[-1][1])
                
            else:
                res.append([start, end])

        return res