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
var reverseList = function(head) {
    function traverse(currentNode, nodesVal){
        if(currentNode === null) return nodesVal;
        nodesVal.push(currentNode.val);
        return traverse(currentNode.next, nodesVal);
    }
    
    const nodesVal = traverse(head, []);
    nodesVal.reverse();
    // console.log(nodesVal);

    let newHead = new ListNode(-1);
    head = newHead;

    nodesVal.forEach(nodeVal => {
        const newNode = new ListNode(nodeVal);
        newHead.next = newNode;
        newHead = newNode;
    });

    // console.log(head.next);
    return head.next;
};