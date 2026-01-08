"""
LeetCode: 2025 12 27 00.29.50 Accepted Runtime 4ms Memory 18.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(log n)
Space Complexity: O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def builder(left, right): 

            if left > right: 
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = builder(left, mid - 1)
            root.right = builder(mid + 1, right)
            return root

        return builder(0, len(nums) - 1)