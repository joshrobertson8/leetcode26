"""
LeetCode: 2025 12 22 13.35.38 Accepted Runtime 0ms Memory 17.6MB

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

        def backtrack(idx, path): 

            if len(path) == len(nums): 
                res.append(path[:])
                return

            for num in nums: 
                if num not in path:
                    path.append(num)
                    backtrack(num + 1, path)
                    path.pop()
            

        backtrack(0, [])

        return res