"""
LeetCode: 2025 01 09 11.08.26 Accepted Runtime 2ms Memory 56.2MB

Algorithm:
Greedy: track tank (current gas) and total (overall gas balance). For each station, update tank and total with gas[i] - cost[i]. If tank becomes negative, reset tank to 0 and set idx to i+1 (can't start from previous index). If total >= 0 at end, return idx (valid starting point), else return -1.

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