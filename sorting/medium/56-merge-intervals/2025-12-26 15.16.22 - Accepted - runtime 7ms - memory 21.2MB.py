"""
LeetCode: 2025 12 26 15.16.22 Accepted Runtime 7ms Memory 21.2MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            
            if res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])

            else:
                res.append([start, end])

        return res

            