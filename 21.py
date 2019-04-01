"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together 
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # one is empty
        if not l1:
            return l2
        if not l2:
            return l1
        # dummy node
        mHead = l1
        # get smaller to the new list
        if l1.val < l2.val:
            mHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            mHead = l2
            mHead.next = self.mergeTwoLists(l1, l2.next)
        return mHead