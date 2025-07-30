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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode mergedListsHead = new ListNode(-1);
		ListNode currNode = mergedListsHead;
		
		while(list1 != null && list2 != null){
			if(list1.val <= list2.val){
				currNode.next = list1;
				list1 = list1.next;
			}
			else{
				currNode.next = list2;
				list2 = list2.next;
			}
			
			currNode = currNode.next;
		}
		
		while(list1 != null){
			currNode.next = list1;
			currNode = currNode.next;
			list1 = list1.next;
		}
		
		while(list2 != null){
			currNode.next = list2;
			currNode = currNode.next;
			list2 = list2.next;
		}
		
		currNode.next = null;
		mergedListsHead = mergedListsHead.next;
		
		return mergedListsHead;
    }
}