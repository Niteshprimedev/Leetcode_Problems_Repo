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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    const rightNodesStack = [];

    let currentNode = root;

    while(currentNode){
        const leftTreeNodes = currentNode.left;
        const rightTreeNodes = currentNode.right;

        if(rightTreeNodes !== null){
            rightNodesStack.push(rightTreeNodes);
        }
        if(leftTreeNodes !== null){
            rightNodesStack.push(leftTreeNodes);
        }
        if(rightNodesStack.length > 0){
            const newNode = rightNodesStack.pop();
            currentNode.left = null;
            currentNode.right = newNode;
            currentNode = currentNode.right;
        }
        else{
            currentNode = currentNode.right;
        }
    }

    // console.log(root);
    return root;
};