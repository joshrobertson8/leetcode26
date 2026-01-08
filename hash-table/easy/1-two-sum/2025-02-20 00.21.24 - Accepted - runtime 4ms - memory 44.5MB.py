"""
LeetCode: 2025 02 20 00.21.24 Accepted Runtime 4ms Memory 44.5MB

Algorithm:
Two-pass hash map using Java: first pass stores each number and its index in HashMap. Second pass, for each number, check if complement exists in map and index differs from current index. Return the two indices. O(n) time with two passes.

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            boolean check = map.containsKey(target - nums[i]);
            if (check && i != map.get(target - nums[i])) {
                return new int[]{i, map.get(target - nums[i])};
            }
        }

        return null;
    }
    
}