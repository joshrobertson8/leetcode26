"""
LeetCode: 2024 10 23 09.31.00 Accepted Runtime 13ms Memory 12.6mb

Algorithm:
Boyer-Moore voting algorithm: maintain a candidate and count. For each number, if count is 0, set candidate to current number. If current number equals candidate, increment count; otherwise decrement. The majority element will survive this process and be the final candidate. Return candidate.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
    
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
    
        return candidate