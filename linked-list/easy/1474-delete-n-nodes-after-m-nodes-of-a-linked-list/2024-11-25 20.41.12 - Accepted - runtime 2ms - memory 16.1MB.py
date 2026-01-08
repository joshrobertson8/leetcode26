"""
LeetCode: 2024 11 25 20.41.12 Accepted Runtime 2ms Memory 16.1MB

Algorithm:
Use prev to track last kept node. Traverse m nodes (keep them), then skip n nodes (delete them). Repeat until end. For each cycle: traverse m nodes updating prev, then traverse n nodes without updating prev, then link prev.next to current. This deletes n nodes after every m nodes.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: Optional[ListNode]
        :type m: int
        :type n: int
        :rtype: Optional[ListNode]
        """
        current = head 
        prev = head

        while current:
            
            mc = m 
            while current and mc > 0:
                prev = current 
                current = current.next
                mc -= 1

            nc = n 
            while current and nc > 0:
                current = current.next
                nc -= 1

            prev.next = current 

        return head

        