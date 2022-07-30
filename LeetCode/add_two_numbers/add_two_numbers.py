# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = res = ListNode(0)

        while l1 or l2:
            s = res.val
            s += l1.val if l1 else 0
            s += l2.val if l2 else 0

            res.val = s % 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if s > 9:
                res.next = ListNode(s // 10)
            elif l1 or l2:
                res.next = ListNode(0)

            res = res.next

        return head
