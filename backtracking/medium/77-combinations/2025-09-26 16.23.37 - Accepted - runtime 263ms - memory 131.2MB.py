"""
LeetCode: 2025 09 26 16.23.37 Accepted Runtime 263ms Memory 131.2MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []


        def backtrack(start, curr):

            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(start, n + 1): 
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(1, [])
        return res