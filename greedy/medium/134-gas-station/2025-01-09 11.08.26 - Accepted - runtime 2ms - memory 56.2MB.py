"""
LeetCode: 2025 01 09 11.08.26 Accepted Runtime 2ms Memory 56.2MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int tank = 0; 
        int total = 0;
        int idx = 0;

        for (int i = 0; i < gas.length; i++) {
            tank += gas[i] - cost[i];
            total += gas[i] - cost[i];

            if (tank < 0) {
                idx = i + 1;
                tank = 0;
            }
        }
        return total >= 0 ? idx : -1;

    }
}