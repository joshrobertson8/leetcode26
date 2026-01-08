"""
LeetCode: 2024 10 07 09.47.56 Accepted Runtime 15ms Memory 11.4MB

Algorithm:
Two-pointer in-place removal: use k as write pointer tracking position for next valid element. Iterate through array with i. If nums[i] != val, write nums[i] to nums[k] and increment k. This removes all occurrences of val in-place, shifting valid elements forward. Return k (new length after removal).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k