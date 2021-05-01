# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res, length = head, 0
        while res:
            res, length = res.next, length + 1
        if n == length:
            return head.next

        res = head
        for i in range(1, length - n):
            res = res.next

        res.next = res.next.next

        return head


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next

        return head
