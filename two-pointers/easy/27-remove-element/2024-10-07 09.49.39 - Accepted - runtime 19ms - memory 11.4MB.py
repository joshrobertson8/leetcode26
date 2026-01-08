"""
LeetCode: 2024 10 07 09.49.39 Accepted Runtime 19ms Memory 11.4MB

Algorithm:
List removal approach: repeatedly count occurrences of val in list and remove them until none remain. Uses list.count() and list.remove() methods. Returns final length. Note: this is inefficient (O(n²)) due to repeated scanning and removal operations.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        while (nums.count(val)):
            nums.remove(val)
        print(nums)
        return len(nums)