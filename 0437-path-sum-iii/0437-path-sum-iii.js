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
 * @return {number}
 */
var pathSum = function(root, targetSum) {

    let totalNumOfPaths = 0;

    function calculatePathSum(currentNode){
        let currPathSum = 0;

        while(currentNode){
            if(currentNode.left === null){
                currPathSum += currentNode.val;

                // Check the current Path sum equals to targetSum or not;
                if(currPathSum === targetSum){
                    totalNumOfPaths += 1;
                }
                currentNode = currentNode.right;
            }
            else{
                prevNode = currentNode.left;
                let depthSum = prevNode.val;

                while(prevNode.right !== null && prevNode.right !== currentNode){
                    prevNode = prevNode.right;
                    depthSum += prevNode.val;
                }

                if(prevNode.right === null){
                    prevNode.right = currentNode;
                    currPathSum += currentNode.val;

                    // Check the current Path sum equals to targetSum or not;
                    if(currPathSum === targetSum){
                        totalNumOfPaths += 1;
                    }
                    currentNode = currentNode.left;
                }
                else{
                    prevNode.right = null;
                    currPathSum -= depthSum;
                    currentNode = currentNode.right;
                }
            }
        }
    }
    function traverse(currentNode){
        // Base Case:
        if(currentNode === null){
            return;
        }

        calculatePathSum(currentNode);

        traverse(currentNode.left);
        traverse(currentNode.right);
    }

    traverse(root);

    return totalNumOfPaths;
};