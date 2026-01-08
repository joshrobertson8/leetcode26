"""
LeetCode: 2025 09 26 16.23.37 Accepted Runtime 263ms Memory 131.2MB

Algorithm:
Backtracking: build combinations of k numbers from 1 to n. Start from a number, add it to the current combination, then recursively build combinations starting from the next number (to avoid duplicates and maintain order). When the combination reaches size k, add it to results. Backtrack by removing the last added number before trying the next option.

Time Complexity: O(n)
Space Complexity: O(n)
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