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
 * @return {number}
 */
var maxPathSum = function(root) {
    const binaryTreeMaxPathSum = [root.val];

    function traverse(currentNode){
        // If currentNode is null;
        if(currentNode === null) return 0;

        let leftTreeMaxSum = traverse(currentNode.left);
        let rightTreeMaxSum = traverse(currentNode.right);

        // Update the leftTreeMaxSum & rightTreeMaxSum;
        leftTreeMaxSum = Math.max(leftTreeMaxSum, 0);
        rightTreeMaxSum = Math.max(rightTreeMaxSum, 0);

        // Update the binary tree max path sum;
        const newBinaryTreeMaxPathSum = currentNode.val + leftTreeMaxSum + rightTreeMaxSum;
        binaryTreeMaxPathSum[0] = Math.max(binaryTreeMaxPathSum[0], newBinaryTreeMaxPathSum);

        // Return the maximum left or right tree sum;
        return currentNode.val + Math.max(leftTreeMaxSum, rightTreeMaxSum);
    }
    traverse(root);

    return binaryTreeMaxPathSum[0];
};