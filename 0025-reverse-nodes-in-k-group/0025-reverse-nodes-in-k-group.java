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
    private ListNode reverseList(ListNode subList){
        ListNode prevNode = null;
        ListNode currNode = subList;
        ListNode nextNode = currNode;

        while(currNode != null){
            nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }

        return prevNode;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        if(k == 1) return head;

        ListNode tailNode = head;
        ListNode currNode = head;

        ListNode dummyListHead = new ListNode(-1);
        ListNode groupRevListP = dummyListHead;

        while(currNode != null){
            tailNode = currNode;

            int idxJ = 1;
            for(int idxI = 1; idxI < k; idxI++){
                if(currNode.next != null){
                    idxJ += 1;
                    currNode = currNode.next;
                }
                else{
                    break;
                }
            }

            ListNode nextNode = null;

            if(currNode != null){
                nextNode = currNode.next;
                currNode.next = null;
            }

            if (idxJ == k){
                ListNode revListHead = reverseList(tailNode);
                groupRevListP.next = revListHead;
            }
            else{
                groupRevListP.next = tailNode;
            }

            groupRevListP = tailNode;
            currNode = nextNode;
        }

        ListNode revListHead = dummyListHead.next;

        return revListHead;
    }
}