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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minPQ = new PriorityQueue<>((a, b) -> a.val - b.val);

        for(ListNode head : lists){
            if(head != null){
                minPQ.add(head);
            }
        }

        ListNode mergedListsHead = new ListNode(-1);
        ListNode currNode = mergedListsHead;

        while(!minPQ.isEmpty()){
            ListNode minNode = minPQ.poll();

            currNode.next = minNode;
            currNode = currNode.next;

            if(minNode.next != null){
                minPQ.add(minNode.next);
            }
        }

        mergedListsHead = mergedListsHead.next;
        return mergedListsHead;
    }
}