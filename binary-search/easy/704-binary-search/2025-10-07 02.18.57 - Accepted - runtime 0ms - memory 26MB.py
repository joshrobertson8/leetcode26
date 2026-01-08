"""
LeetCode: 2025 10 07 02.18.57 Accepted Runtime 0ms Memory 26MB

Algorithm:
Recursive binary search: define a helper function that takes low and high indices. If low > high, return -1 (not found). Calculate mid. If nums[mid] equals target, return mid. If nums[mid] > target, recursively search left half. Otherwise, recursively search right half. Start with the full array range.

Time Complexity: O(n)
Space Complexity: O(n)
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