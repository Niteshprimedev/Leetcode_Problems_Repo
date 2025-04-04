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
var preorderTraversal = function(root) {
    // Morris Preorder Traversal
    // Logic: Root -> Left -> Right
    // Case1: If the left node is null then print left & go to right
    // Case2: If the left node is not null, then before going to the leftSubTree,
    // make a thread connection to the current node from the right most node of the
    // leftSubTree and then go left
    // Case3: If the thread is already connected, then remove the thread connection

    const preOrderTraversal = [];
    let currentNode = root;

    while(currentNode !== null){
        // Case1: If the leftNode is null, then print root & go right
        if(currentNode.left === null){
            preOrderTraversal.push(currentNode.val);
            currentNode = currentNode.right;
        }
        // Case2: If the leftNode is not null, then make a thread connnection first
        else{
            let prevRootNode = currentNode.left;
            while(prevRootNode.right !== null && prevRootNode.right !== currentNode){
                prevRootNode = prevRootNode.right;
            }
            // If the thread connection is not connected to currentNode then connect it;
            if(prevRootNode.right === null){
                prevRootNode.right = currentNode;
                preOrderTraversal.push(currentNode.val);
                currentNode = currentNode.left;
            }
            // If the thread is already connected then remove it;
            else{
                prevRootNode.right = null;
                currentNode = currentNode.right;
            }
        }
    }

    return preOrderTraversal;
};