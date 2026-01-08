"""
LeetCode: 2024 12 21 20.26.25 Accepted Runtime 36ms Memory 12.6mb

Algorithm:
Use a while loop with a count tracker. For each position, if the current element equals the previous one, increment count. If count exceeds 2, remove the duplicate using pop() and adjust the index. Otherwise, reset count to 1 for a new element. This allows at most 2 occurrences of each element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        count = 1

        while i < len(nums):

            if nums[i] == nums[i - 1]:
                count += 1

                if count > 2:
                    nums.pop(i)
                    i -= 1
                    count -= 1
            else: 
                count = 1
            i += 1
        return len(nums)