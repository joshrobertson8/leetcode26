"""
LeetCode: 2025 10 26 18.49.05 Accepted Runtime 3ms Memory 18.9MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        d = [1] * n

        for i in range(1, n): 

            if nums[i] > nums[i - 1]: 
                d[i] = d[i - 1] + 1

        return max(d)