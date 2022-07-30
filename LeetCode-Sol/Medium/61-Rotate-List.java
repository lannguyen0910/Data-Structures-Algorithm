/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null){
            return head;
        }
        
        Stack<ListNode> stack = new Stack<>();
        ListNode curr = head;
        while (curr != null){
            stack.push(curr);
            curr = curr.next;
        }
        
        int rotate = k % stack.size();
        for(int i=0; i < rotate; i++){
            ListNode node = stack.pop();
            
            node.next = head;
            head = node;
            
            ListNode lastNode = stack.peek();
            lastNode.next = null;
        }
        
        
        return head;
    }
}