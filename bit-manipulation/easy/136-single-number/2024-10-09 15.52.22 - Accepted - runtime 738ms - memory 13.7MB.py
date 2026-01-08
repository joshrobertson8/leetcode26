"""
LeetCode: 2024 10 09 15.52.22 Accepted Runtime 738ms Memory 13.7mb

Algorithm:
Use a list to track seen numbers. For each number, if it's not in the list, add it. If it's already in the list, remove it. After processing all numbers, the list contains only the single number that appeared once. This approach uses O(n) space but is conceptually simpler.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def singleNumber(self, nums):
        
        seen = []

        for i in nums:
            if i not in seen:
                seen.append(i)
            else:
                seen.remove(i)
        return seen[0]