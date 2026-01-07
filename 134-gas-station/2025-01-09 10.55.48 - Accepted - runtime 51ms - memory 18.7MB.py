"""
LeetCode: 2025 01 09 10.55.48 Accepted Runtime 51ms Memory 18.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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