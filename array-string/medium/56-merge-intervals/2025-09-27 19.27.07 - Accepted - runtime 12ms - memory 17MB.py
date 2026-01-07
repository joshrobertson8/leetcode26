"""
LeetCode: 2025 09 27 19.27.07 Accepted Runtime 12ms Memory 17mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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