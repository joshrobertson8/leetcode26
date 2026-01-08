"""
LeetCode: 2025 01 23 10.36.53 Accepted Runtime 0ms Memory 12.5MB

Algorithm:
Two-pointer swap approach: use i to scan and n to track valid length. When nums[i] == val, swap with last valid element (nums[n-1]) and decrement n (effectively removing val). Otherwise increment i. This removes val in-place by swapping with elements from the end. Return n (new length).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 
        n = len(nums)

        while i < n:

            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n     