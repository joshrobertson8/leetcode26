"""
LeetCode: 2025 07 28 11.28.33 Accepted Runtime 235ms Memory 17.9MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        maxOr = 0 

        for num in nums: 
            maxOr |= num
        
        def backtrack(idx, curOr): 

            nonlocal count, maxOr

            if idx == len(nums):
                
                if curOr == maxOr: 
                    count += 1
                    
                return 
            
            backtrack(idx + 1, curOr)

            backtrack(idx + 1, curOr | nums[idx])

        backtrack(0, 0)
        return count 