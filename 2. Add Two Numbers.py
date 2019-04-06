"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return

        n1, n2 = self.getNumOfLink(l1), self.getNumOfLink(l2)
        # 反转
        n = str(n1+n2)[::-1]
        head = cur= ListNode(n[0])
        for i in range(1, len(n)):
            cur.next = ListNode(n[i])
            cur = cur.next
        return head
    # 由链表求数字
    def getNumOfLink(self, head):
        i = res = 0
        while head:
            res = res + head.val * (10 ** i)
            head = head.next
            i += 1
        return res