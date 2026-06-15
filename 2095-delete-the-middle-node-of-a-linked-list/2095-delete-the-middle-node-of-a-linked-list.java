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
    public ListNode deleteMiddle(ListNode head) {
        if(head == null || head.next == null) return null;

        ListNode slowNode = head;
        ListNode fastNode = head;
        ListNode prevNode = head;

        while(fastNode != null && fastNode.next != null){
            prevNode = slowNode;
            slowNode = slowNode.next;
            fastNode = fastNode.next.next;
        }

        if(prevNode != null){
            prevNode.next = slowNode.next;
            slowNode.next = null;
        }

        return head;
    }
}