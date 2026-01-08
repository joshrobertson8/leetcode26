"""
LeetCode: 2025 02 20 00.21.24 Accepted Runtime 4ms Memory 44.5MB

Algorithm:
TODO: Describe your approach here

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