"""
LeetCode: 2025 08 31 17.19.07 Accepted Runtime 1057ms Memory 21.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if len(nums) <= 1: 
            return nums

        middle = len(nums) // 2

        leftArray = self.sortArray(nums[:middle])
        rightArray = self.sortArray(nums[middle:])

        return self.merge(leftArray,rightArray)


    def merge(self, leftArray, rightArray): 
        i = j = 0 
        res = []

        while i < len(leftArray) and j < len(rightArray): 

            if leftArray[i] <= rightArray[j]:
                res.append(leftArray[i])
                i += 1
            else: 
                res.append(rightArray[j])
                j += 1

        res.extend(leftArray[i:])
        res.extend(rightArray[j:])

        return res