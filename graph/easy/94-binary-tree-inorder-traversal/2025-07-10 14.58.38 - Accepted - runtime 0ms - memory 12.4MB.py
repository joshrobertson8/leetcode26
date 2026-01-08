"""
LeetCode: 2025 07 10 14.58.38 Accepted Runtime 0ms Memory 12.4MB

Algorithm:
Iterative inorder traversal using stack: while current node exists or stack is not empty, go left as far as possible (pushing nodes to stack). Pop from stack, append value to result, then move to right subtree. This simulates recursive traversal without recursion.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = [] 
        current = root
        stack = []

        while current or stack: 
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result