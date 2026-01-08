"""
LeetCode #0: , next=none):

Problem:
Definition for singly-linked list.
class ListNode(object):
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
Since list is sorted, duplicates are adjacent. Traverse with current pointer. If current.val == current.next.val, skip next node by setting current.next = current.next.next. Otherwise, advance current. This removes duplicates in-place.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def deleteDuplicates(self, head):
        
        current = head 

        

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head