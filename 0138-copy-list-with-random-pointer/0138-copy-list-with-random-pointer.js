/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

 class Node{
    constructor(val){
        this.val = val;
        this.next = null;
        this.random = null;
    }
 }

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function(head) {

    // Logic:
    // To create a hashmap with the original linked list's node as the key
    // and the newNode as the value without any next & random pointers
    // Then loop through the original linked list
    // Get the newNode for the currentNode of the original linked list
    // Get the nextNode from the currentNode's next node's value in the hashmap
    // & update the newNode's next pointer to it
    // Get the randomNode from the currentNode's random node's value in the hashmap
    // & update the newNode's random pointer to it;

    // Pseudocode;

    // Create a Node class with val, next, and random variables;
    // Create a nodesKeyCopyNodesValHashmap variable and initialize it to an emtpy map
    // Create a currentNode variable and initialize it to head
    // Run a while loop as long as the currentNode is not null or in other words the until the 
    // linked list is not traversed
    // Create a newNode variable and initialize it to new Node(val) with the currentNode's
    // val
    // Update the hashmap with the currentNode as the key and newNode as the value
    // without any next and random pointers;
    // Move the currentNode pointer to the currentNode.next node;
    // Update the nodesKeyCopyNodesValHashmap with the currentNode as the key
    // and null as the value;
    // Reset the currentNode to point to the head again for next
    // and random pointers copy
    // Run a while loop as long as the currentNode is not null or in other words until
    // the linked list is not traversed
    // Createa a copyNode variable and initialize it to the currentNode's value in the
    // hashmap
    // Create a copiedNextNode variable and initialize it to the currentNode's next
    // node's value in the hashmap
    // Create a copiedRandomNode variable and initialize it to the currentNode's random
    // node's value in the hashmap
    // Update the copiedNode.next pointer to the copiedNextNode
    // Update the copiedNode.random pointer to the copiedRandomNode
    // Move the currentNode pointer to the currentNode.next node
    // Create a copiedList and initialize it to the head node's value in the hashmap
    // Empty the hashmap as we don't require it
    // Finally, we will have the copy list with random pointer in the copiedList variable
    // so will return it;

    const nodesKeyCopyNodesValHashmap = new Map();

    let currentNode = head;

    while(currentNode){
        const newNode = new Node(currentNode.val);

        nodesKeyCopyNodesValHashmap.set(currentNode, newNode);
        currentNode = currentNode.next;
    }

    nodesKeyCopyNodesValHashmap.set(currentNode, null);
    // console.log(nodesKeyCopyNodesValHashmap);

    currentNode = head;

    while(currentNode){
        const copiedNode = nodesKeyCopyNodesValHashmap.get(currentNode);
        const copiedNextNode = nodesKeyCopyNodesValHashmap.get(currentNode.next);
        const copiedRandomNode = nodesKeyCopyNodesValHashmap.get(currentNode.random);

        copiedNode.next = copiedNextNode;
        copiedNode.random = copiedRandomNode;

        currentNode = currentNode.next;
    }

    const copiedList = nodesKeyCopyNodesValHashmap.get(head);
    nodesKeyCopyNodesValHashmap.clear();

    // console.log(nodesKeyCopyNodesValHashmap);

    // console.log("Time Complexity: 0(N) + 0(N) => 20(N) or 0(N) ");
    // console.log("Space Complexity: Linked List Length");

    return copiedList;
};