# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        p1 = head
        p2 = head
        isCycle = False
#       check if cysle exists
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                isCycle = True
                break
        
#       find index of intersection
        if isCycle:
            curr = head
            while curr is not p1:
                curr = curr.next
                p1 = p1.next
            return curr
        else:
            return None
