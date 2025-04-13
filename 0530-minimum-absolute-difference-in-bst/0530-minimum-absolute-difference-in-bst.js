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
var getMinimumDifference = function(root) {

    // Root to left, Root too right of left
    // Root to Right; Root to left of right
    let minAbsNodesDiff = Infinity;
    let prevNode = null;

    function traverse(currentNode){
        // Base Case:
        if(currentNode === null){
            return;
        }

        traverse(currentNode.left);

        if(prevNode !== null){
            const minNodeDiffVal = currentNode.val - prevNode.val;
            minAbsNodesDiff = Math.min(minAbsNodesDiff, minNodeDiffVal);
        }
        prevNode = currentNode;

        traverse(currentNode.right);
    }
    traverse(root);

    return minAbsNodesDiff;
};