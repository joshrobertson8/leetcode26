"""
LeetCode: 2025 09 25 22.56.19 Accepted Runtime 10ms Memory 17.2mb

Algorithm:
Greedy algorithm.

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

        merged = [intervals[0]] 

        for start, end in intervals[1:]: 

            lastEnd = merged[-1][1]

            if start <= lastEnd: 
                merged[-1][1] = max(lastEnd, end)
            else: 
                merged.append([start, end])
        return merged