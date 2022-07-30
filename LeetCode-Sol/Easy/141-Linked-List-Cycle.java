/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null){
            return false;
        }
        HashSet <ListNode> hashTable=new HashSet<>();
        while(head != null) {
            if(hashTable.contains(head)) {
                return true;
            }
            hashTable.add(head);
            head = head.next;
        }
        return false;
    }
}