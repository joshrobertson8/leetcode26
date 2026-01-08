"""
LeetCode: 2025 12 22 12.55.58 Accepted Runtime 3ms Memory 17.4MB

Algorithm:
Backtracking: build permutations by trying each number that hasn't been used yet. For each position, try adding an unused number to the current path, recursively build the rest, then backtrack by removing it. When the path length equals the input length, we have a complete permutation. Use a list to track the current path and check membership to avoid duplicates.

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