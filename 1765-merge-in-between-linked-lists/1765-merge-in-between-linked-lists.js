/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeInBetween = function(list1, a, b, list2) {
    let prevNode = null;
    let currentNode = list1;
    let nextNode = currentNode.next;

    let list2TailNode = list2;

    for(let idxI = 0; idxI < a; idxI++){
        if(idxI === a){
            break;
        }
        prevNode = currentNode;
        currentNode = currentNode.next;
    }

    for(let idxI = a; idxI < b; idxI++){
        if(idxI === b){
            break;
        }
        currentNode = currentNode.next;
    }

    nextNode = currentNode.next;

    while(list2TailNode.next){
        list2TailNode = list2TailNode.next;
    }

    list2TailNode.next = nextNode;
    prevNode.next = list2;

    return list1;
};