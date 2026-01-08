"""
LeetCode: 2025 08 31 17.19.07 Accepted Runtime 1057ms Memory 21.8mb

Algorithm:
Merge sort: recursively divide array into halves until base case (length <= 1). Merge sorted halves by comparing elements from both arrays, appending smaller element. Continue until one array is exhausted, then append remaining elements. This sorts the array using divide-and-conquer approach.

Time Complexity: O(n)
Space Complexity: O(n)
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