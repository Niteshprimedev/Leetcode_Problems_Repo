/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    // Same Rotation & Reverse Logic is used here:

    let linkedListLen = 0;
    const tailNode = head;

    let currentNode = head;
    while(currentNode){
        currentNode = currentNode.next;
        linkedListLen += 1;
    }

    k = k % linkedListLen;

    if(k === 0 || head === null) return head;

    let newHead = head; 
    currentNode = newHead;

    let revNodeIdx = k + 1;

    while(revNodeIdx < linkedListLen){
        currentNode = currentNode.next;
        revNodeIdx += 1;
    }
    // console.log(linkedListLen, revNodeIdx);

    const currentNodeNextNode = currentNode.next;
    currentNode.next = null;
    currentNode = currentNodeNextNode;

    newHead = reverseList(tailNode);
    prevNode = reverseList(currentNode);

    tailNode.next = prevNode;

    newHead = reverseList(newHead);

    function reverseList(newHead){
        if(newHead === null) return newHead;
        // console.log(newHead);

        let prevNode = null;
        let newCurrentNode = newHead;
        let nextNode = newCurrentNode.next;

        while(newCurrentNode){
            nextNode = newCurrentNode.next;
            newCurrentNode.next = prevNode;
            prevNode = newCurrentNode;
            newCurrentNode = nextNode;
        }

        return prevNode;
    }

    return newHead;
};