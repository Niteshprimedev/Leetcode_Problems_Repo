/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let mergedListHead = list1;

    if(list1 === null || list2 === null){
        return list1 || list2;
    }

    let list1NodeVal = list1.val;
    let list2NodeVal = list2.val;

    if(list2NodeVal < list1NodeVal){
        mergedListHead = list2;
        list2 = list2.next;
    }
    else{
        list1 = list1.next;
    }

    let currentNode = mergedListHead;

    while(list1 && list2){
        let list1NodeVal = list1.val;
        let list2NodeVal = list2.val;

        if(list1NodeVal <= list2NodeVal){
            currentNode.next = list1;
            currentNode = list1;
            list1 = list1.next;
        }
        else{
            currentNode.next = list2;
            currentNode = list2;
            list2 = list2.next;
        }
    }

    if(list1 !== null){
        currentNode.next = list1;
    }
    else if(list2 !== null){
        currentNode.next = list2;
    }

    return mergedListHead;
};