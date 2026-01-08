"""
LeetCode: 2025 12 27 00.29.50 Accepted Runtime 4ms Memory 18.5MB

Algorithm:
Recursive builder: if left > right, return None (base case). Find middle index. Create root with nums[mid]. Recursively build left subtree from left to mid-1, right subtree from mid+1 to right. This creates balanced BST by always choosing middle element as root, ensuring height balance.

Time Complexity: O(n)
Space Complexity: O(n)
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