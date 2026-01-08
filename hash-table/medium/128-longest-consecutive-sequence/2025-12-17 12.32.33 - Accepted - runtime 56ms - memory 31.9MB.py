"""
LeetCode: 2025 12 17 12.32.33 Accepted Runtime 56ms Memory 31.9MB

Algorithm:
Sort the array first. Maintain a count of current consecutive sequence. Skip duplicates. If current number equals previous + 1, increment count. Otherwise, update maximum count and reset to 1. Return the maximum consecutive count found. This finds longest consecutive sequence after sorting.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sNums = nums.sort()
        count, mCount = 1, 1

        if not nums: 
            return 0

        for i in range(1, len(nums)): 

            if nums[i] != nums[i - 1]: 
            
                if nums[i - 1] + 1 == nums[i]: 
                    count += 1
            
                else: 
                    mCount = max(mCount, count)
                    count = 1
        
        return max(count, mCount)