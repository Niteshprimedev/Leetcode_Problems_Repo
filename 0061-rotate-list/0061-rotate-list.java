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
    private ListNode reverseList(ListNode newHead){
        if(newHead == null) return newHead;
        ListNode prevNode = null;
        ListNode currNode = newHead;
        ListNode nextNode = currNode.next;

        while(currNode != null){
            nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }

        return prevNode;
    }

    public ListNode rotateRight(ListNode head, int k) {
        /*
        int linkedListLen = 0;
        ListNode currNode = head;

        while(currNode != null){
            linkedListLen += 1;
            currNode = currNode.next;
        }

        k = k % linkedListLen;

        if(k == 0 || head == null) return head;

        ListNode newNode = head;
        currNode = newNode;
        ListNode tailNode = head;

        int revNodeIdx = k + 1;

        while(revNodeIdx < linkedListLen){
            currNode = currNode.next;
            revNodeIdx += 1;
        }

        // Reverse (n - k) nodes to n nodes;
        ListNode currNodeNextNode = currNode.next;
        currNode.next = null;

        ListNode nextNode = reverseList(currNodeNextNode); // 11 -> 12 -> null

        // Reverse 0 to (n - k) nodes;
        newHead = reverseList(head); // 1 to 10 nodes -> null

        tailNode.next = nextNode; // 10 to 1.next => (12 -> 11 -> null)

        newHead = reverseList(newHead); // reverse from 10 to -> 1 and -> 12 -> 11 -> null

        return newHead;
        */

        // Meta Prep Time Practice:
        int linkedListLen = 0;
        ListNode currNode = head;

        while(currNode != null){
            linkedListLen += 1;
            currNode = currNode.next;
        }

        k = linkedListLen > 0 ? k % linkedListLen : k;

        if(k == 0 || head == null) return head;

        // Reverse the entire list (0 to N) nodes;
        ListNode newHead = reverseList(head);

        // Reverse first k nodes (0 to k) nodes;
        int revNodeIdx = 1;
        currNode = newHead;

        while(revNodeIdx < k){
            currNode = currNode.next;
            revNodeIdx += 1;
        }

        ListNode currNodeNextNode = currNode.next;
        currNode.next = null;

        ListNode tailNode = newHead;
        newHead = reverseList(newHead);

        // Reverse next (k + 1) to N nodes;
        ListNode nextNode = reverseList(currNodeNextNode);
        tailNode.next = nextNode;

        return newHead;
    }
}