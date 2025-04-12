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

    // Better: Iterative Preoorder and Memoization;
    // Logic: To track the currPathSum while traversing the tree
    // And each new node check whether currPathSum - targetSum is already exist in 
    // oldPathSumHashmap or not?
    // oldPathSumHashmap is the mapping of whatever path sum we've generated while traversing
    // and their frequency;
    // Note: The currentPathSum can also be the targetSum so count for 0 
    // cause currPathSum - targetSum will give 0;

    const oldPathSumFreqMap = new Map();
    oldPathSumFreqMap.set(0, 1);

    let totalNumOfPaths = 0;

    let currentNode = root;
        
    // Recursive Preorder Calculation;
    function traverse(currentNode, currPathSum){
        // Base Case:
        if(currentNode === null){
            return 0;
        }

        currPathSum += currentNode.val;
        const oldPathSum = currPathSum - targetSum;

        totalNumOfPaths += oldPathSumFreqMap.get(oldPathSum) || 0;
        const hashValue = (oldPathSumFreqMap.get(currPathSum) || 0) + 1;

        oldPathSumFreqMap.set(currPathSum, hashValue);
        traverse(currentNode.left, currPathSum);
        traverse(currentNode.right, currPathSum);

        const updatedValue = (oldPathSumFreqMap.get(currPathSum) || 0) - 1;
        oldPathSumFreqMap.set(currPathSum, updatedValue);
    }
    traverse(root, 0);

    // console.log(oldPathSumFreqMap);
    return totalNumOfPaths;
    
    /** 
    // Brute Force Solution;
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
    */
};