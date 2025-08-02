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
    private static ListNode reverseList(ListNode subHead, int left, int right){
        ListNode prevNode = null;
        ListNode currNode = subHead;
        ListNode nextNode = currNode;

        int idx = left;

        while(currNode != null && idx <= right){
            nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
            idx += 1;
        }

        if(subHead != null){
            subHead.next = nextNode;
        }

        return prevNode;
    }

    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(left == right){
            return head;
        }

        ListNode prevNode = null;;
        ListNode currNode = head;
        int idx = left - 1;

        while(idx > 0 && currNode != null){
            prevNode = currNode;
            currNode = currNode.next;
            idx -= 1;
        }

        if(prevNode != null){
            prevNode.next = reverseList(currNode, left, right);
        }
        else{
            head = reverseList(currNode, left, right);
        }

        return head;
    }
}