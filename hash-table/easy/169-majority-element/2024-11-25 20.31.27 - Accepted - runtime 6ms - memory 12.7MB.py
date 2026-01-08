"""
LeetCode: 2024 11 25 20.31.27 Accepted Runtime 6ms Memory 12.7mb

Algorithm:
Build frequency map counting occurrences of each number. Return the number with maximum frequency using max() with key=hashmap.get. This finds the element that appears more than n/2 times.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}

        for i in nums:
            
            if i in hashmap:
                hashmap[i] += 1

            else:
                hashmap[i] = 1

        return max(hashmap, key=hashmap.get)