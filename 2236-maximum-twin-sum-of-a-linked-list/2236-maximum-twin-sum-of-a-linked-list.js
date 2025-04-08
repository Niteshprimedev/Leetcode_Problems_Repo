/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function(head) {
    // Using the reverse logic;
    let maxTwinSum = 0;
    let prevNode = null;
    let slowNode = head;
    let fastNode = head;
    let currentNode = head;

    while(fastNode && fastNode.next){
        // Move slowNode to the middle node
        slowNode = slowNode.next;
        fastNode = fastNode.next.next;

        // Start reversing the first half of the linked list
        currentNode.next = prevNode;
        prevNode = currentNode;
        currentNode = slowNode;
    }

    // Loop through the second half of the list and get + check the twins sum;
    while(slowNode){
        const newMaxTwinSum = prevNode.val + slowNode.val;
        maxTwinSum = Math.max(maxTwinSum, newMaxTwinSum);

        // Update the slowNode & prevNode to keep the loop going till the end node;
        slowNode = slowNode.next;
        prevNode = prevNode.next;
    }

    return maxTwinSum;
};