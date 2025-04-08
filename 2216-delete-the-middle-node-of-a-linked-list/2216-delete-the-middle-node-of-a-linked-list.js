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
var deleteMiddle = function(head) {
    if(head.next === null) return null;

    let prevNode = head;
    let slowNode = head;
    let fastNode = head;

    // Loop to get to the middle node and the node before the middle node to delete it
    while(fastNode && fastNode.next){
        prevNode = slowNode;
        slowNode = slowNode.next;
        fastNode = fastNode.next.next;
    }

    // Delete the middle node by updating the prevNode pointer;
    prevNode.next = slowNode.next;
    slowNode.next = null;

    return head;
};