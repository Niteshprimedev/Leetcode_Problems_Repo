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
var swapPairs = function(head) {
    /** 
    // A single node or no node is already swapped or nothing to swap;
    if (head === null || head.next === null){
        return head;
    }

    let prevNode = head;
    let currentNode = head.next;
    let nextNode = currentNode;

    head = head.next;

    while(currentNode){
        nextNode = currentNode.next;

        // Swap the adjacent nodes:
        currentNode.next = prevNode;
        prevNode.next = nextNode;

        if(nextNode && nextNode.next){
            // if the nextNode exists then set the prevNode.next to its next;
            prevNode.next = nextNode.next;

            currentNode = nextNode.next;
            prevNode = nextNode;
        }
        else{
            break;
        }
    }

    return head
    */

    // Shardha Didi Solution: Clean Code - 
    if(head === null || head.next === null){
        return head;
    }

    let prevNode = null;
    let firstNode = head;
    let secondNode = head.next;

    while(firstNode !== null && secondNode !== null){
        // Swap the first and second nodes:
        let thirdNode = secondNode.next;

        secondNode.next = firstNode;
        firstNode.next = thirdNode;

        if(prevNode === null){
            head = secondNode;
        }
        else{
            prevNode.next = secondNode;
        }

        prevNode = firstNode;
        firstNode = thirdNode;
        if(thirdNode){
            secondNode = thirdNode.next;
        }
    }

    return head;
};