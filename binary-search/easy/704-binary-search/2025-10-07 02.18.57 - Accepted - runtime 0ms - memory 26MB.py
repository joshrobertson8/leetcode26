"""
LeetCode: 2025 10 07 02.18.57 Accepted Runtime 0ms Memory 26MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binarySearch(low, high): 

            if low > high: 
                return -1

            mid = (low + high) // 2

            if nums[mid] == target: 
                return mid

            if nums[mid] > target: 
                return binarySearch(low, mid - 1)
            
            else: 
                return binarySearch(mid + 1, high)

        return binarySearch(0, len(nums) - 1)