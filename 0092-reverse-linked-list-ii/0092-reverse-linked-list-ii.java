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
    /*
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
    */
    public ListNode reverseBetween(ListNode head, int left, int right) {
        /*
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
    */
    
        ListNode prevNode = null;
		ListNode currNode = head;
		
		int idx;
		
		for(idx = 1; idx < left; idx++){
			prevNode = currNode;
			currNode = currNode.next;
		}
		
		ListNode reverseNode = null;
		ListNode nextNode = currNode;
		
		for(idx = left; idx <= right; idx++){
			nextNode = currNode.next;
			
			currNode.next = reverseNode;
			reverseNode = currNode;
			currNode = nextNode;
		}
		
		if(prevNode == null){
			nextNode = head;
			prevNode = reverseNode;
			head = prevNode;
		}
		else{
			nextNode = prevNode.next;
			prevNode.next = reverseNode;
		}
		
		nextNode.next = currNode;
		
		return head;
    }
}