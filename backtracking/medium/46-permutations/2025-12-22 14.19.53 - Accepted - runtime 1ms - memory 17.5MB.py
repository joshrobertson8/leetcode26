"""
LeetCode: 2025 12 22 14.19.53 Accepted Runtime 1ms Memory 17.5MB

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