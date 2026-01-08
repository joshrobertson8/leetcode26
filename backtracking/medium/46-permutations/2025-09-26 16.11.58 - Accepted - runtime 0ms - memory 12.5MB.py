"""
LeetCode: 2025 09 26 16.11.58 Accepted Runtime 0ms Memory 12.5MB

Algorithm:
Stack-based approach.

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
                return

            for num in nums: 
                if num not in curr: 
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()



        backtrack([])
        return res
