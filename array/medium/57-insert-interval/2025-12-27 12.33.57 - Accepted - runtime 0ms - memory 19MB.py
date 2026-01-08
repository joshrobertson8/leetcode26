"""
LeetCode: 2025 12 27 12.33.57 Accepted Runtime 0ms Memory 19MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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