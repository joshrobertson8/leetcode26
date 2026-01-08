"""
LeetCode: 2025 12 29 08.18.44 Accepted Runtime 11ms Memory 24.3MB

Algorithm:
Iterate through each index.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        a = [0] * n

        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a