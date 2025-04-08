/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    const nodesLessThanXHead = new ListNode(-1);
    const nodesGreaterThanEqualXHead = new ListNode(-1);

    // console.log(nodesGreaterThanEqualXHead.next);

    let currentNode = head;
    let lessThanXNode = nodesLessThanXHead;
    let greaterThanXNode = nodesGreaterThanEqualXHead;

    while(currentNode){
        const currentNodeVal = currentNode.val;

        if(currentNodeVal < x){
            lessThanXNode.next = currentNode;
            lessThanXNode = lessThanXNode.next;
        }
        else{
            greaterThanXNode.next = currentNode;
            greaterThanXNode = greaterThanXNode.next;
            // console.log(greaterThanXNode);
        }
        currentNode = currentNode.next;
    }

    greaterThanXNode.next = null;

    lessThanXNode.next = nodesGreaterThanEqualXHead.next; // skipping the dummy nodes -1 that's why .next;
    
    // console.log("Head", nodesLessThanXHead, lessThanXNode);
    head = nodesLessThanXHead.next;

    return head;
};