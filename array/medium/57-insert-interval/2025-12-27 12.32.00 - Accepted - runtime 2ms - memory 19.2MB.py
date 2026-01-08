"""
LeetCode: 2025 12 27 12.32.00 Accepted Runtime 2ms Memory 19.2MB

Algorithm:
Iterate through existing intervals. If an interval ends before the new interval starts, add it to result. If an interval starts after the new interval ends, add the new interval and then set the new interval to the current one. If intervals overlap, merge by updating the new interval's start and end to encompass both. Finally, append the merged new interval.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for start, end in intervals:

            if end < newInterval[0]:
                res.append([start, end])

            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end]

            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        res.append(newInterval)
        return res