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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    // Logic: Solution using BFS -> Tree wise BFS;
    // 
    // console.log('To Do: To try out without actually deleting the ndoes from queue');
    // Source Link: https://leetcode.com/problems/most-profitable-path-in-a-tree/description/?envType=daily-question&envId=2025-02-24
    // Pre-requisite: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
    if(root === null) return [];

    const queue = [];
    let currentNode = root;
    let currentNodeIdx = 0;
    const bfsLeverOrderTraversal = [];

    queue.push(currentNode);

    while(queue.length && currentNodeIdx < queue.length){
        let rowLength = queue.length;
        const treeLevelTraversal = [];

        for(let idxI = currentNodeIdx; idxI < rowLength; idxI++){
            currentNode = queue[currentNodeIdx++];

            const currentNodeVal = currentNode.val;
            treeLevelTraversal.push(currentNodeVal);

            if(currentNode.left) queue.push(currentNode.left);
            if(currentNode.right) queue.push(currentNode.right);
        }

        bfsLeverOrderTraversal.push(treeLevelTraversal);
    }

    // console.log(queue, currentNodeIdx, bfsLeverOrderTraversal);

    return bfsLeverOrderTraversal;

    /** 
    while(queue.length && root !== null){
        let rowLength = queue.length;
        const treeLevelTraversal = [];

        for(let idxI = 0; idxI < rowLength; idxI++){
            currentNode = queue.shift();

            const currentNodeVal = currentNode.val;
            treeLevelTraversal.push(currentNodeVal);

            if(currentNode.left) queue.push(currentNode.left);
            if(currentNode.right) queue.push(currentNode.right);
        }

        bfsLeverOrderTraversal.push(treeLevelTraversal);
    }

    return bfsLeverOrderTraversal;
    */
};