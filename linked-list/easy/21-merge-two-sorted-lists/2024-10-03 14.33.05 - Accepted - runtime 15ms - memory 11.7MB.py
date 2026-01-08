"""
LeetCode: 2024 10 03 14.33.05 Accepted Runtime 15ms Memory 11.7mb

Problem:
class ListNode:
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
Continue while window is valid.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def mergeTwoLists(self, list1, list2):

        # initilize head 
        dummy = ListNode()
        current = dummy

        # merge lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
            list1 = list1.next
        elif list2:
            current.next = list2
            list2 = list2.next
        
        return dummy.next