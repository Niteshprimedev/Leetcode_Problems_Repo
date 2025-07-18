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
 * @return {boolean}
 */
var isValidBST = function(root) {
    // Solution using inOrder Traversal & Strictly Increasing Problem:
    // Problem 1: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
    // Problem 2: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
    // Problem 3: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

    /**
    // Solution 1: Using next and curr element comparison
    const inOrderTraversal = [];
    let isValidBinarySearchTree = true;

    // Perform inorder traversal on the tree and get the nodeVals
    function traverse(currentNode){
        if(currentNode.left) traverse(currentNode.left);

        inOrderTraversal.push(currentNode.val);

        if(currentNode.right) traverse(currentNode.right);
    }
    traverse(root);

    // Check if the inorder traversal of the given tree is
    // strictly increasing or not?
    for(let idxI = 0; idxI < inOrderTraversal.length - 1; idxI++){
        const currNodeVal = inOrderTraversal[idxI];
        const nextNodeVal = inOrderTraversal[idxI + 1];

        // inorder traversal is not strictly increasing...
        if(nextNodeVal <= currNodeVal){
            // Since the inorder traversal is not strictly increasing 
            // so it's not a valid BST
            isValidBinarySearchTree = false;
            break;
        }
    }

    return isValidBinarySearchTree;
    */
    
    /**
    // Solution 2: Using curr and prev element comparison
    const inOrderTraversal = [];
    let isValidBinarySearchTree = true;

    // Perform inorder traversal on the tree and get the nodeVals
    function traverse(currentNode){
        if(currentNode.left) traverse(currentNode.left);

        inOrderTraversal.push(currentNode.val);

        if(currentNode.right) traverse(currentNode.right);
    }
    traverse(root);

    // Check if the inorder traversal of the given tree is
    // strictly increasing or not?
    for(let idxI = 1; idxI < inOrderTraversal.length; idxI++){
        const prevNodeVal = inOrderTraversal[idxI - 1];
        const currNodeVal = inOrderTraversal[idxI];

        // inorder traversal is not strictly increasing...
        if(currNodeVal <= prevNodeVal){
            // Since the inorder traversal is not strictly increasing 
            // so it's not a valid BST
            isValidBinarySearchTree = false;
            break;
        }
    }

    return isValidBinarySearchTree;
    */

    /**
    // Solution 3: Using Morris Traversal
    // Logic: Root -> Left -> Right
    // Case1: If the left node is null then print node & go to rightSubTree
    // Case2: If the left node is not null, then before going to the leftSubTree,
    // make a thread connection to the current node from the right most node of the
    // leftSubTree and then go to leftSubTree
    // Case3: If the thread is already connected, then remove the thread connection

    let isValidBinarySearchTree = true;
    let currentNode = root;
    const inOrderTraversal = [];

    while (currentNode){
        // Case1: If the leftNode is null, then print root & go right
        if(currentNode.left === null){
            inOrderTraversal.push(currentNode.val);
            currentNode = currentNode.right
        }
        else{
            // Case2: If the leftNode is not null, then make a thread connnection first
            let prevRootNode = currentNode.left;
            while(prevRootNode.right && prevRootNode.right !== currentNode){
                prevRootNode = prevRootNode.right;
            }
            // If the thread connection is not connected to currentNode then connect it;
            if(prevRootNode.right === null){
                prevRootNode.right = currentNode;
                currentNode = currentNode.left;
            }
            // If the thread is already connected then remove it;
            else{
                prevRootNode.right = null;
                inOrderTraversal.push(currentNode.val);
                currentNode = currentNode.right;
            }
        }
    }

    for(let idxI = 1; idxI < inOrderTraversal.length; idxI++){
        const prevNodeVal = inOrderTraversal[idxI - 1];
        const currentNodeVal = inOrderTraversal[idxI];

        if(currentNodeVal <= prevNodeVal){
            isValidBinarySearchTree = false;
            break;
        }
    }

    return isValidBinarySearchTree;
    */

    // Solution 4: Comparing with parent and children
    // Solution using constant space by leveraging
    // the Binary Search Properties;


    function traverse(currentNode, leftVal, rightVal){
        if(currentNode === null){
            return true;
        }
        const leftTree = traverse(currentNode.left, leftVal, currentNode.val);
        const rightTree = traverse(currentNode.right, currentNode.val, rightVal);

        // console.log(currentNode, leftVal, rightVal);
        let isCurrentNode = true;

        if(currentNode){
            if(currentNode.val <= leftVal || currentNode.val >= rightVal){
                isCurrentNode = false;
            }
        }
        if(leftTree && rightTree && isCurrentNode){
            return true;
        }
        else{
            return false;
        }
    }
    return traverse(root, -Infinity, Infinity);
};