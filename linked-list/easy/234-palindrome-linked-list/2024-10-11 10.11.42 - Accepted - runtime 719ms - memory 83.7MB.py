"""
LeetCode #0: , next=none):

Problem:
Definition for singly-linked list.
class ListNode(object):
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
Traverse the linked list to collect values into an array, then compare with its reverse.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isPalindrome(self, head):
        current = head
        arr = []

        while current:
            arr.append(current.val)
            current = current.next
        
        r_arr = arr[::-1]

        if r_arr == arr:
            return True
        return False