"""
LeetCode: 2026 01 01 17.34.17 Accepted Runtime 27ms Memory 17.5MB

Algorithm:
Backtracking: try including the current candidate (can reuse it) or skipping to the next. Track the current path and its sum. If sum equals target, add path to result. If sum exceeds target or we've exhausted candidates, backtrack. When including a candidate, we can reuse it (same index), allowing multiple uses of the same number.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(idx, path):
            
            if sum(path) == target:
                res.append(path[:])
                return
            
            
            if sum(path) >= target or idx > len(candidates) - 1:
                return
            path.append(candidates[idx])
            backtrack(idx, path)
            path.pop()

            backtrack(idx + 1, path)
        
        
        backtrack(0, [])
        return res
        
        