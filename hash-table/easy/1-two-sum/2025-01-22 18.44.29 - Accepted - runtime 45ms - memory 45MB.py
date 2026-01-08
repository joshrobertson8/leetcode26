"""
LeetCode: 2025 01 22 18.44.29 Accepted Runtime 45ms Memory 45MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++){
            for (int j = i+1; j < nums.length; j++){
                if (nums[j] == target-nums[i]) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {};
    }
}