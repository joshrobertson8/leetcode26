"""
LeetCode: 2026 01 03 16.58.34 Accepted Runtime 4ms Memory 21.4MB

Algorithm:
Sort intervals by start time. Initialize result with first interval. For each subsequent interval, if it overlaps with last interval in result (start <= res[-1][1]), merge by updating end to max of both ends. Otherwise, append as new interval. This merges all overlapping intervals.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]


        for start, end in intervals[1:]:

            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])

            else:
                res.append([start, end])
        return res