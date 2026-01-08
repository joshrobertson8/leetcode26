"""
LeetCode: 2025 12 22 14.19.53 Accepted Runtime 1ms Memory 17.5MB

Algorithm:
TODO: Describe your approach here

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

        def backtrack(path): 

            if len(path) == len(nums): 
                res.append(path[:])
                return

            for num in nums: 
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
            

        backtrack([])

        return res