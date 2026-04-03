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
    public ListNode partition(ListNode head, int x) {
        // Partitoning List => 

        // [3 1  5 80 3 2 1] => x => 4
        // arrSmaller = [1 3 3 2 1]
        // arrGreaterEquals = [5 80]

        // [3 1 3 2 1 5 80] => ans? 


        // head = [1,4,3,2,5,2], x = 3
        // Make two dummy list like we create empty arrays;
        ListNode smallerThanXHead = new ListNode(-1);
        ListNode greaterAndEqualThanX = new ListNode(-1);

        // Create two pointers to traverse and connect the nodes
        // like we do using indices array
        ListNode smallerP = smallerThanXHead;
        ListNode greaterP = greaterAndEqualThanX;

        ListNode currNode = head;

        while(currNode != null){
            if(currNode.val < x){
                // first attach the node
                smallerP.next = currNode;

                // then move the pointer as this position
                // is already filled so take next position
                smallerP = smallerP.next;
                // idx += 1
            }
            else{
                greaterP.next = currNode;
                greaterP = greaterP.next;
            }

            currNode = currNode.next;
        }

        // [1 1 1 1] -> next => [3]
        // [3 3 33]
        smallerP.next = greaterAndEqualThanX.next;
        greaterP.next = null; // 5 -> 2 => I have to change
        // the pointer to null;

        ListNode partitionList = smallerThanXHead.next;

        return partitionList;
    }
}