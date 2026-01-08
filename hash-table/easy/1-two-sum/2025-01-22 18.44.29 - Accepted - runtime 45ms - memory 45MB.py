"""
LeetCode: 2025 01 22 18.44.29 Accepted Runtime 45ms Memory 45MB

Algorithm:
Brute force using Java: nested loops check all pairs (i, j) where j > i. If nums[j] == target - nums[i], return [i, j]. This is O(n^2) time complexity, checking every possible pair combination.

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