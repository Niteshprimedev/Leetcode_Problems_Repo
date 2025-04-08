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
    let prevNode = head;
    let slowNode = head;
    let fastNode = head;
    let maxTwinSum = 0;

    while(fastNode && fastNode.next){
        prevNode = slowNode;
        slowNode = slowNode.next;
        fastNode = fastNode.next.next;
    }

    prevNode.next = null;
    const reversedListHead = reverseList(slowNode);

    // console.log(reversedListHead, slowNode.next, slowNode, prevNode);
    function reverseList(newHead){
        
        let newPrevNode = null;
        let newCurrentNode = newHead;
        let newNextNode = newCurrentNode.next;

        while(newCurrentNode){
            newNextNode = newCurrentNode.next;
            newCurrentNode.next = newPrevNode;
            newPrevNode = newCurrentNode;
            newCurrentNode = newNextNode;
        }

        // console.log(newHead, newPrevNode);
        return newPrevNode;
    }

    slowNode = head;
    fastNode = reversedListHead;

    while(slowNode){
        const newMaxTwinSum = slowNode.val + fastNode.val;
        maxTwinSum = Math.max(maxTwinSum, newMaxTwinSum);

        slowNode = slowNode.next;
        fastNode = fastNode.next;
    }

    return maxTwinSum;
};