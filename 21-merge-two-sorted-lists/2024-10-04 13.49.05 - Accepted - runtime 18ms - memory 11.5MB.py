"""
LeetCode: 2024 10 04 13.49.05 Accepted Runtime 18ms Memory 11.5mb

Problem:
class ListNode:
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        # set the head
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else: 
            head = list2
            list2 = list2.next
        
        current = head
        
        # merge the lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                current.next = list2
                list2 = list2.next
            current = current.next
        # remaining vals

        if list1:
            current.next = list1
            list1 = list1.next
        if list2:
            current.next = list2
            list2 = list2.next
        return head