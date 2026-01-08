"""
LeetCode: 2026 01 01 17.49.02 Accepted Runtime 35ms Memory 28.7MB

Algorithm:
Use Counter to count frequencies of all numbers in nums. Then iterate through numbers 1 to len(nums). If a number is not in the counter (frequency is 0), it's missing - add it to result. Return list of all missing numbers.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        hashmap = Counter(nums)

        for num in range(1, len(nums) + 1):
            if num not in hashmap:
                res.append(num)
        return res