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
var countNodes = function(root) {
    // Logic: We keep on traversing the tree, and calculating its left and right subtrees height
    // and we found the leftHeight equals to the rightHeight then it means this subTree or the tree
    // is a complete tree and hence we can calculate the number of nodes with the properties of a
    // complete tree: just using 2^h - 1 nodes
    // And we can stop traversing further in that subtree or tree once we know that it is a complete tree;
    // Solution in O(LogN^2) Time Complexity;

    let currentNode = root;

    function traverse(currentNode){
        if(currentNode === null){
            return 0;
        }

        const leftHeight = leftTreeHeight(currentNode);
        const rightHeight = rightTreeHeight(currentNode);

        let nodesCount = Math.pow(2, leftHeight) - 1;

        if(leftHeight === rightHeight){
            return nodesCount;
        }
        else{
            const leftTreeHeight = traverse(currentNode.left);
            const rightTreeHeight = traverse(currentNode.right);
            nodesCount = 1 + leftTreeHeight + rightTreeHeight;
            return nodesCount;
        }
    }
    return traverse(root);

    function leftTreeHeight(currentNode){
        let currHeight = 0;
        while(currentNode){
            currHeight += 1;
            currentNode = currentNode.left;
        }

        return currHeight;
    }

    function rightTreeHeight(currentNode){
        let currHeight = 0;
        while(currentNode){
            currHeight += 1;
            currentNode = currentNode.right;
        }

        return currHeight;
    }

    /** 
    // Solution in O(N) Time Complexity;
    let totalNodesCount = 0;

    function traverse(currentNode){
        if (currentNode === null){
            return 0;
        }

        const leftNodesCount = traverse(currentNode.left);
        const rightNodesCount = traverse(currentNode.right);

        return 1 + leftNodesCount + rightNodesCount;
    }
    totalNodesCount = traverse(root);

    return totalNodesCount;
    */
};