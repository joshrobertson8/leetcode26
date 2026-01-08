"""
LeetCode: 2025 01 03 17.16.29 Accepted Runtime 2ms Memory 45MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        // Correct casing for Integer
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            // Correct usage of map.get()
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };  // Fixed syntax
            }

            map.put(nums[i], i);
        }

        // Throw an exception if no solution is found
        throw new IllegalArgumentException("No two sum solution");
    }
}
