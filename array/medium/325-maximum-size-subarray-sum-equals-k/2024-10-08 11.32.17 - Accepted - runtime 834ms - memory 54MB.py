"""
LeetCode: 2024 10 08 11.32.17 Accepted Runtime 834ms Memory 54mb

Algorithm:
Use prefix sum technique with a hash map. Track cumulative sums and their earliest indices. For each position, if cumulative_sum equals k, update max_len. If (cumulative_sum - k) exists in the map, we found a subarray summing to k; update max_len with the length. Only store the earliest index for each cumulative sum to maximize subarray length.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        sum_map = {}
        summ = 0
        max_len = 0
        
        for i in range(len(nums)):
            summ += nums[i]
            
            if summ == k:
                max_len = i + 1
            
            if summ - k in sum_map:
                max_len = max(max_len, i - sum_map[summ - k])
            
            if summ not in sum_map:
                sum_map[summ] = i
        
        return max_len