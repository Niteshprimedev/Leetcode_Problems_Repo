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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    function traverse(currentNode, currPathSum, targetSum){

        // Base Case;
        if(currentNode === null) return false;

        currPathSum += currentNode.val;
        const isLeftTreePathSum = traverse(currentNode.left, currPathSum, targetSum);
        if(isLeftTreePathSum) return true;
        const isRighTreePathSum = traverse(currentNode.right, currPathSum, targetSum);
        if(isRighTreePathSum) return true;

        if(currentNode.left === null && currentNode.right === null){
            // Path sum condition;
            if(currPathSum === targetSum) return true;
            return false;
        }
        return isLeftTreePathSum || isRighTreePathSum;
    }
    return traverse(root, 0, targetSum);
};