"""
LeetCode: 2025 12 22 14.19.34 Accepted Runtime 0ms Memory 17.2MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        def backtrack(idx, path): 

            if idx == len(nums): 
                res.append(path[:])
                return

            # include
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()

            backtrack(idx + 1, path)

        backtrack(0, [])
        return res