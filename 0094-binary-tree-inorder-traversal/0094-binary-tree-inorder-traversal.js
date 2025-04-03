/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    // InOrder Traversal => left + root + right;
    // Morris Traversal Logic:
    // 1) Case1: If left node is null, print currentNode, and go right
    // 2) Case2: Before going to left, make the right most node on leftSubTree connected to currentNode, and then go left
    // 3) Case3: If thread is already pointing to the currentNode, then remove the thread;
    const inOrderTraversal = [];

    let currentNode = root;
    while(currentNode !== null){
        // If the currentNode or root has no leftSubTree;
        if(currentNode.left === null){
            // Print the currentNodes value
            inOrderTraversal.push(currentNode.val);
            // And move to the rightSubTree;
            currentNode = currentNode.right;
        }
        // If the currentNode or root has leftSubTree;
        else{
            let prevRootNode = currentNode.left;
            // Move to the rightmost node of the first leftSubTree;
            while(prevRootNode.right !== null && prevRootNode.right !== currentNode){
                prevRootNode = prevRootNode.right;
            }

            // Make the thread connection to the currentNode if not threaded yet
            if(prevRootNode.right === null){
                prevRootNode.right = currentNode;
                currentNode = currentNode.left;
            }
            // Else remove the thread connection to the currentNode
            else{
                prevRootNode.right = null;
                inOrderTraversal.push(currentNode.val);
                currentNode = currentNode.right;
            }
        }
    }

    return inOrderTraversal;
};