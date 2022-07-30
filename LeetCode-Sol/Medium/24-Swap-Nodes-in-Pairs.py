# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        
        dummy = ListNode(next = head)
        p = dummy
        head = head.next
        
        
        while p.next and p.next.next:
        
            post = p.next.next.next
            
            p1 = p.next
            p2 = p.next.next
            
            p.next = p2
            p1.next = post
            p2.next = p1

            p = p1
            
        return head