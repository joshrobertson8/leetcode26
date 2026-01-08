"""
LeetCode: 2026 01 01 17.49.02 Accepted Runtime 35ms Memory 28.7MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        hashmap = Counter(nums)

        for num in range(1, len(nums) + 1):
            if num not in hashmap:
                res.append(num)
        return res