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
    private ListNode reverseList(ListNode remHead){
        ListNode prevNode = null;
        ListNode currNode = remHead;
        ListNode nextNode = remHead;

        while(currNode != null){
            nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }
        return prevNode;
    }
    
    public boolean isPalindrome(ListNode head) {
        // Logic: Reach the half of the list;
        // Reverse the next half to compare both in one go => Two Pointers;

        // Edge Cases;
        if(head == null || head.next == null){
            return true;
        }


        // Two Nodes or more than two;
        ListNode prevNode = head;
        ListNode slowNode = head;
        ListNode fastNode = head;

        while(fastNode != null && fastNode.next != null){
            prevNode = slowNode;
            slowNode = slowNode.next;
            fastNode = fastNode.next.next;
        }

        prevNode.next = null;

        ListNode reversedHead = reverseList(slowNode);

        slowNode = head;
        fastNode = reversedHead;

        while(slowNode != null){
            if(slowNode.val != fastNode.val){
                return false;
            }

            slowNode = slowNode.next;
            fastNode = fastNode.next;
        }

        return true;
    }
}