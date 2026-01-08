"""
LeetCode #0: , next=none):

Problem:
Definition for singly-linked list.
class ListNode(object):
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
Continue while window is valid.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Create a dummy node
        current = dummy  # Pointer to build the new list
        
        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next  # Advance list1
            else:
                current.next = list2
                list2 = list2.next  # Advance list2
            current = current.next  # Move current
        
        # Attach the remaining part of the list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next  # Return the merged list (skipping the dummy node)