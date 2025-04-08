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
    if(head === null || head.next === null) return head;

    let oddNodesList = head;
    let evenNodesList = head.next;

    let oddListPointer = oddNodesList;
    let evenListPointer = evenNodesList;

    let currentNode = evenNodesList.next;
    while(currentNode){
        oddListPointer.next = currentNode;
        oddListPointer = currentNode;

        currentNode = currentNode.next;

        evenListPointer.next = currentNode;

        if(currentNode){
            evenListPointer = currentNode;
            currentNode = currentNode.next;
        }
    }

    evenListPointer.next = null;
    oddListPointer.next = evenNodesList;

    head = oddNodesList;

    return head;
};