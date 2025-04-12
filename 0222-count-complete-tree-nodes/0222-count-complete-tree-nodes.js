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
    /**
            If we know the height of the tree, the only other information needed to determine the number of nodes is the number of nodes in the last level. The rest of the levels are completely filled and it can be calculated just by knowing the value of the height of the tree.
        Determine the height of the tree by traversing the leftmost path, i.e, root to root->left to root->left->left and so on. This takes O(logn) time.
        Then, we will binary search to determine which node is the last node in the last level. More precisely, we need to find the number of nodes in the last level.
        We initialize left = 0 and right = n/2-1 (this is the maximum number of nodes that the last level can have). Then, we use binary search to find whether the mid-th node exists in the tree (i.e. if it is non-null). Each of this operation takes O(logn) time.
        In this way find the right-most non-null node in the last level. There will be O(logn) such operations and hence, the total complexity amounts to O((logn)^2).
    */
    // Logic: We keep on traversing the tree, and calculating its left and right subtrees height
    // and we found the leftHeight equals to the rightHeight then it means this subTree or the tree
    // is a complete tree and hence we can calculate the number of nodes with the properties of a
    // complete tree: just using 2^h - 1 nodes
    // And we can stop traversing further in that subtree or tree once we know that it is a complete tree;
    let maxDepth = 0;
    currentNode = root;

    function traverse(currentNode){
        if(currentNode === null){
            return 0;
        }

        const leftHeight = leftTreeHeight(currentNode);
        const rightHeight = rightTreeHeight(currentNode);

        let nodesCount = leftHeight;

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

        currHeight = Math.pow(2, currHeight) - 1;
        return currHeight;
    }

    function rightTreeHeight(currentNode){
        let currHeight = 0;
        while(currentNode){
            currHeight += 1;
            currentNode = currentNode.right;
        }

        currHeight = Math.pow(2, currHeight) - 1;
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