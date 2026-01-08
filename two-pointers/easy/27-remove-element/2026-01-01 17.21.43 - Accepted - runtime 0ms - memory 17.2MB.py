"""
LeetCode: 2026 01 01 17.21.43 Accepted Runtime 0ms Memory 17.2MB

Algorithm:
Two pointers: write pointer tracks position to write next valid element. Iterate through array: if nums[i] != val, write nums[i] to nums[write] and increment write. This removes all occurrences of val in-place, returning new length (write).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1

        return write