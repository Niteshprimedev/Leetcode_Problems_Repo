/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode currNode1 = headA;
		ListNode currNode2 = headB;
		
		while(currNode1 != currNode2){
			currNode1 = currNode1 != null ? currNode1.next : headB;
			currNode2 = currNode2 != null ? currNode2.next : headA;
		}
		
		return currNode1;
    }
}