# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        
        head = ListNode()
        curr = head
        
        if not p1 and not p2:
            return head.next
        
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            elif p2.val < p1.val:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
            else:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
                
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        
        if p1:
            while p1:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
        else:
            while p2:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
                
        return head.next