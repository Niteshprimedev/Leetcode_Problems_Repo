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
    public ListNode detectCycle(ListNode head) {
        ListNode slowNode = head;
		ListNode fastNode = head;
		
		while(fastNode != null && fastNode.next != null){
			slowNode = slowNode.next;
			fastNode = fastNode.next.next;
			
			if(slowNode == fastNode){
				break;
			}
		}
		
		if(fastNode == null || fastNode.next == null){
			return null;
		}
		
		slowNode = head;
		
		while(slowNode != fastNode){
			slowNode = slowNode.next;
			fastNode = fastNode.next;
		}
		
		return slowNode;
    }
}