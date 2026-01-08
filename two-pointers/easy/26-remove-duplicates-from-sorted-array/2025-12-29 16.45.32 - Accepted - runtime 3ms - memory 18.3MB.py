"""
LeetCode: 2025 12 29 16.45.32 Accepted Runtime 3ms Memory 18.3MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 0
        n = len(nums)
        count = 1
        write = 1

        if n == 1:
            return 1

        while r < n:

            while r < n and nums[l] == nums[r]:
                r += 1

            if r == n:
                break

            count += 1
            nums[write] = nums[r]
            write += 1
            l = r

        return count