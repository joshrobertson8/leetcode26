"""
LeetCode: 2025 10 01 20.03.44 Accepted Runtime 3ms Memory 12.6MB

Algorithm:
Use a recursive helper function to explore all possibilities.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(curr):

            if len(curr) == len(nums): 
                res.append(curr[:])

            for n in nums: 

                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()
        
        
        backtrack([])

        return res