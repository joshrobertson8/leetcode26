"""
LeetCode: 2025 12 30 15.31.45 Accepted Runtime 19ms Memory 17.3MB

Algorithm:
Stack-based approach.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, path):
            total = sum(path)

            if total == target:
                res.append(path[:])
                return

            if total > target or idx == len(candidates):
                return

            path.append(candidates[idx])
            backtrack(idx, path)
            path.pop()
            
            backtrack(idx + 1, path)


        backtrack(0, [])
        return res