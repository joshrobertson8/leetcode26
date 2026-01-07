"""
LeetCode: 2025 10 01 20.03.43 Accepted Runtime 3ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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