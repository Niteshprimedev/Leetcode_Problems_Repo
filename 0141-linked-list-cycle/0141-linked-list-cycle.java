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
        /*
        ListNode slowNode = head;
        ListNode fastNode = head;

        while(fastNode != null && fastNode.next != null){
            slowNode = slowNode.next;
            fastNode = fastNode.next.next;

            if(slowNode == fastNode){
                return true;
            }
        }

        return false;
        */

        // Using HashMap
        // Meta Prep Time Practice
        HashMap<ListNode, Boolean> seenMap = new HashMap<>();

        ListNode currNode = head;

        while(currNode != null){
            seenMap.put(currNode, true);
            currNode = currNode.next;

            if(seenMap.containsKey(currNode)) return true;
        }

        return false;
    }
}