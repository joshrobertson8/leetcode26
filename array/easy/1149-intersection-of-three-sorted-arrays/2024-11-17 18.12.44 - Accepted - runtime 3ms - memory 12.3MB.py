"""
LeetCode: 2024 11 17 18.12.44 Accepted Runtime 3ms Memory 12.3mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(len(arr1)):
            if arr1[i] in hashmap:  # Fixed syntax: removed 'is'
                hashmap[arr1[i]] += 1
            else:
                hashmap[arr1[i]] = 1
        for i in range(len(arr2)):
            if arr2[i] in hashmap:
                hashmap[arr2[i]] += 1
            else:
                hashmap[arr2[i]] = 1
        for i in range(len(arr3)):
            if arr3[i] in hashmap:
                hashmap[arr3[i]] += 1
            else:
                hashmap[arr3[i]] = 1

        # Use a list comprehension to collect keys where value equals 3
        return [key for key, value in hashmap.items() if value == 3]