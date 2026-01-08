"""
LeetCode: 2026 01 01 17.34.17 Accepted Runtime 27ms Memory 17.5MB

Algorithm:
TODO: Describe your approach here

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
        
        