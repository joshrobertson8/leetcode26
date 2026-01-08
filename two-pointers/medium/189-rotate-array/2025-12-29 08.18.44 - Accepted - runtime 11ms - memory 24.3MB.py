"""
LeetCode: 2025 12 29 08.18.44 Accepted Runtime 11ms Memory 24.3MB

Algorithm:
Extra array approach: create new array a of size n. For each index i, place nums[i] at position (i+k) % n in a. Copy a back to nums. This rotates array right by k positions by mapping each element to its new position. Requires O(n) extra space.

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