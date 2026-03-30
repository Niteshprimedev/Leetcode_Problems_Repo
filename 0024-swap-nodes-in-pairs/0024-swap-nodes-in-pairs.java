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
    public ListNode swapPairs(ListNode head) {
        // Meta Prep Time Practice:
        if(head == null || head.next == null){
            return head;
        }

        ListNode prevNode = null;
        ListNode firstNode = head;
        ListNode secondNode = head.next;

        while(firstNode != null && secondNode != null){
            ListNode thirdNode = secondNode.next;

            secondNode.next = firstNode;
            firstNode.next = thirdNode;

            if(prevNode == null){
                head = secondNode;
            }
            else{
                prevNode.next = secondNode;
            }

            prevNode = firstNode;
            firstNode = thirdNode;

            if(thirdNode != null){
                secondNode = thirdNode.next;
            }
        }

        return head;
    }
}