"""
LeetCode: 2025 12 22 14.19.34 Accepted Runtime 0ms Memory 17.2MB

Algorithm:
Backtracking: for each element, we have two choices - include it or exclude it. At each index, first include the current element, recurse to the next index, then backtrack by removing it and recurse without it. When we reach the end of the array, add the current path (subset) to the result. This generates all 2^n subsets.

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