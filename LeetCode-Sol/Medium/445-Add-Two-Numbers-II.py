# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        ret = []
        
#       add into stack
        p1 = l1
        while p1:
            s1.append(p1.val)
            p1 = p1.next
        p2 = l2
        while p2:
            s2.append(p2.val)
            p2 = p2.next

#       convert to same size
        less = []
        more = []
        if len(s1)<len(s2):
            less = s1
            more = s2
        else:
            less = s2
            more = s1
        while len(less) < len(more):
            less.insert(0, 0)
        
        carry = 0
        while len(less)>0:
            val = less.pop() + more.pop() + carry
            num = val % 10
            carry = val // 10
            ret.insert(0, num)
        
        if carry>0:
            ret.insert(0, carry)
        
        head = ListNode(ret.pop(0))
        curr = head
        while len(ret)>0:
            curr.next = ListNode(ret.pop(0))
            curr = curr.next
        
        return head