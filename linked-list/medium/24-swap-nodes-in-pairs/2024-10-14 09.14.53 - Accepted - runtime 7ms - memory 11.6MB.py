"""
LeetCode: 2024 10 14 09.14.53 Accepted Runtime 7ms Memory 11.6MB

Algorithm:
Handle empty or single-node lists. Traverse list in pairs. For each pair, swap values (not nodes). Move current two steps forward. This swaps adjacent nodes by value, simpler than node pointer manipulation.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        
        if not head:
            return 
    
        if not head.next:
            return head

        current = head
        
        while current and current.next:
            temp_val = current.val
            next_node_val = current.next.val
            current.val = next_node_val
            current.next.val = temp_val
            
            current = current.next.next
        return head

