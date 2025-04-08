/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let slowNode = head;
    let fastNode = head;
    let prevNode = null;

    for(let nodeIdx = 0; nodeIdx < n; nodeIdx++){
        fastNode = fastNode.next;
    }

    while(fastNode){
        prevNode = slowNode;
        slowNode = slowNode.next;
        fastNode = fastNode.next;
    }

    if(prevNode === null) return head.next;

    prevNode.next = slowNode.next;
    slowNode.next = null;

    return head;
    /** 
    if(n === 1 && head.next === null) return null;

    let linkedListLen = 0;
    let currentNode = head;

    while(currentNode){
        currentNode = currentNode.next;
        linkedListLen += 1;
    }

    let deletingNodeIdx = linkedListLen - n;
    let prevNode = head;
    currentNode = head;

    // console.log(deletingNodeIdx, linkedListLen);

    for(let nodeIdx = 0; nodeIdx < deletingNodeIdx; nodeIdx++){
        prevNode = currentNode;
        currentNode = currentNode.next;
    }

    prevNode.next = currentNode.next;
    currentNode.next = null;

    return head;
    */
};