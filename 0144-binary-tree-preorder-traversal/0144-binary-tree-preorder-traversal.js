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
    // Iterative Preorder;
    const preOrderTraversal = [];
    const rightLeftNodesStack = [];
    let currentNode = root;

    while(currentNode){
        preOrderTraversal.push(currentNode.val);

        if(currentNode.right !== null){
            rightLeftNodesStack.push(currentNode.right);
        }
        if(currentNode.left !== null){
            rightLeftNodesStack.push(currentNode.left);
        }
        
        if(rightLeftNodesStack.length > 0){
            currentNode = rightLeftNodesStack.pop();
        }
        else{
            currentNode = currentNode.left;
        }
    }

    return preOrderTraversal;
};