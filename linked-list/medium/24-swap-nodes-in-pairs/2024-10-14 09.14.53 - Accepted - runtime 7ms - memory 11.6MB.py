"""
LeetCode #0: , next=none):

Problem:
Definition for singly-linked list.
class ListNode(object):
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

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