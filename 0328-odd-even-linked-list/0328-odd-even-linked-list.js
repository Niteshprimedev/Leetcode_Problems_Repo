/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    // 1-based Indexing for odd and even linked list;
    let dummyList1 = new ListNode(-1);
    let dummyList2 = new ListNode(-1);

    let oddNodesList = dummyList1;
    let evenNodesList = dummyList2;

    let currentNode = head;
    let indices = 1;

    while(currentNode){
        if(indices % 2 !== 0){
            // Indice is odd; and odd starts from index 1
            oddNodesList.next = currentNode;
            oddNodesList = currentNode;
        }
        else{
            // When indice is even; and odd starts from index 2
            evenNodesList.next = currentNode;
            evenNodesList = currentNode;
        }
        indices += 1;
        currentNode = currentNode.next;
    }

    evenNodesList.next = null;
    oddNodesList.next = dummyList2.next;

    head = dummyList1.next;
    return head;
};