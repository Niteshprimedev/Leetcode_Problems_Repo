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
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
    const pathSumEqualsTargetAllPaths = [];

    function traverse(currentNode, currPathSum, currPathNodesArr){
        if(currentNode === null){
            return;
        }
        const currentNodeVal = currentNode.val;

        currPathSum += currentNodeVal;

        currPathNodesArr.push(currentNodeVal);

        traverse(currentNode.left, currPathSum, [...currPathNodesArr]);
        traverse(currentNode.right, currPathSum, [...currPathNodesArr]);

        // Leaf node condition;
        if(currentNode.left === null && currentNode.right === null){
            const isPathSumEqual = currPathSum === targetSum;
            if(isPathSumEqual){
                pathSumEqualsTargetAllPaths.push(currPathNodesArr);
            }
        }
    }

    traverse(root, 0, []);

    return pathSumEqualsTargetAllPaths;
};