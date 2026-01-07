"""
LeetCode: 2025 09 25 20.18.37 Accepted Runtime 3ms Memory 12.5mb

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
                return

            
            for num in nums: 
                if num not in curr: 
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])

        return res