"""
LeetCode: 2024 10 08 11.23.07 Accepted Runtime 803ms Memory 54.2mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        # Dictionary to store the cumulative sum and its earliest index
        sum_map = {}
        cumulative_sum = 0
        max_len = 0
        
        # Iterate through the nums array
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            
            # If the cumulative sum equals k, update max_len to the current index + 1
            if cumulative_sum == k:
                max_len = i + 1
            
            # If (cumulative_sum - k) is in the map, we have a subarray summing to k
            if cumulative_sum - k in sum_map:
                max_len = max(max_len, i - sum_map[cumulative_sum - k])
            
            # Only add cumulative_sum to the map if it's not already present
            if cumulative_sum not in sum_map:
                sum_map[cumulative_sum] = i
        
        return max_len