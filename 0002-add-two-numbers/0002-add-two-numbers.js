/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let currentNode;

    let list1NumVal = reverseList(l1);
    let list2NumVal = reverseList(l2);

    function reverseList(newHead){
        let prevNode = null;
        currentNode = newHead;
        let nextNode = currentNode.next;

        while(currentNode){
            nextNode = currentNode.next;
            currentNode.next = prevNode;
            prevNode = currentNode;
            currentNode = nextNode;
        }

        const strNumVal = listToNumStr(prevNode);
        return strNumVal;
    }

    function listToNumStr(currentNode){
        let listNumVal = '';

        while(currentNode){
            const currentNodeVal = currentNode.val;
            listNumVal += currentNodeVal;
            currentNode = currentNode.next;
        }

        return listNumVal;
    }
    
    list1NumVal = BigInt(list1NumVal);
    list2NumVal = BigInt(list2NumVal);
    const numVal = list1NumVal + list2NumVal;

    // console.log(numVal);

    const numValStr = numVal.toString();
    let twoNumSumList = new ListNode(-1);
    currentNode = twoNumSumList;

    let idxI = numValStr.length - 1;

    for(let numStr of numValStr){
        const numVal = Number(numValStr[idxI]);
        const newNode = new ListNode(numVal);
        currentNode.next = newNode;
        currentNode = newNode;

        idxI -= 1;
    }

    twoNumSumList = twoNumSumList.next;
    return twoNumSumList;
};