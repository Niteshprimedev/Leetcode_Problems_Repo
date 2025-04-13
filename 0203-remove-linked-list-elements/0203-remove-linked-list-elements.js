/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    if(head === null) return head;

    function removeNodes(prevNode, currentNode){
        // Base Case:
        if(currentNode === null){
            prevNode.next = null;
            return head;
        }

        if(currentNode.val === val){
            currentNode = currentNode.next;
        }
        else{
            prevNode.next = currentNode;
            prevNode = currentNode;
            currentNode = currentNode.next;
        }

        removeNodes(prevNode, currentNode);
        
        return head;
    }
    removeNodes(head, head.next);

    if(head !== null && head.val === val){
        head = head.next;
    }
    return head;
};