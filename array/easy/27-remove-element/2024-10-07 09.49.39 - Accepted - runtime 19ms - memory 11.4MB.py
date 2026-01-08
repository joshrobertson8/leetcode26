"""
LeetCode: 2024 10 07 09.49.39 Accepted Runtime 19ms Memory 11.4mb

Algorithm:
Repeatedly check if val exists in the array using count(), and if it does, remove one occurrence using remove(). Continue until no more occurrences of val remain. This approach is simpler but less efficient due to repeated array operations.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        while (nums.count(val)):
            nums.remove(val)
        print(nums)
        return len(nums)