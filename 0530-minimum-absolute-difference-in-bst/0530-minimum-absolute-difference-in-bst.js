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
    /**
    // Solution 1: Recursive InOrder Traversal
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
    */

    // Solution 2: Recursive InOrder Traversal
    // Morris Traversal: Iterative Inorder Traversal;

    // Step1: If left node is null then take the min_diff and go to right
    // Step2: If the left node is not null then before taking min_diff &
    // going to the left_subtree, make a threaded connection to the current_node
    // with the rightmost node of the left_subtree. 
    // Step3: If the threaded connection is already made then remove the connection
    // and go the right_subtree;

    let minAbsNodesDiff = Infinity;

    let prevNode = null;
    let currentNode = root;

    while (currentNode !== null){
        // we are at the root level;
        if(currentNode.left === null){
            // Take the minDiff, update prevNode to currentNode
            if(prevNode !== null){
                const newMinAbsNodesDiff = Math.abs(currentNode.val - prevNode.val);
                minAbsNodesDiff = Math.min(minAbsNodesDiff, newMinAbsNodesDiff)
            }
            prevNode = currentNode;
            // move currentNode to the right_subtree
            currentNode = currentNode.right;
        }
        else{
            let rightMostNode = currentNode.left;

            while(rightMostNode.right !== null && rightMostNode.right !== currentNode){
                rightMostNode = rightMostNode.right;
            }

            if(rightMostNode.right === null){
                rightMostNode.right = currentNode;
                currentNode = currentNode.left;
            }
            else{
                rightMostNode.right = null;
                
                // Take the minDiff, update prevNode to currentNode
                if(prevNode !== null){
                    const newMinAbsNodesDiff = Math.abs(currentNode.val - prevNode.val);
                    minAbsNodesDiff = Math.min(minAbsNodesDiff, newMinAbsNodesDiff)
                }
                prevNode = currentNode;
                currentNode = currentNode.right;
            }
        }
    }

    return minAbsNodesDiff
};