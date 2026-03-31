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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return head;
        if(head.next == null) return head;

        ListNode sortedHead = new ListNode(-101);

        ListNode currNode = head;
        ListNode nextNode = head.next;
        ListNode distNode = sortedHead;

        while(nextNode != null){
            if(nextNode.val == currNode.val){
                while(nextNode != null && nextNode.val == currNode.val){
                    nextNode = nextNode.next;
                }

                currNode = nextNode;
            }
            else{
                distNode.next = currNode;
                distNode = distNode.next;
                currNode = currNode.next;
            }

            if(nextNode != null){
                nextNode = nextNode.next;
            }
        }

        distNode.next = currNode;

        return sortedHead.next;
    }
}