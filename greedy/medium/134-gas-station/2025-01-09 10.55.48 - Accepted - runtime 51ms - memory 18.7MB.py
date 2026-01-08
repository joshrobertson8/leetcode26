"""
LeetCode: 2025 01 09 10.55.48 Accepted Runtime 51ms Memory 18.7mb

Algorithm:
Greedy: track tank (current gas) and total (overall gas balance). For each station, update tank and total with gas[i] - cost[i]. If tank becomes negative, reset tank to 0 and set index to i+1 (can't start from previous index). If total >= 0 at end, return index (valid starting point), else return -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        total = 0
        index = 0 

        for i in range(len(gas)):

            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if tank < 0: 
                index = i + 1
                tank = 0

        return index if total >= 0 else -1