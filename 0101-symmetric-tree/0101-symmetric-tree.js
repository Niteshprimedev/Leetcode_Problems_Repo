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
var isSymmetric = function(root) {
    if(root.left === null && root.right === null) return true

    function traverse(currentNode){
        if(currentNode === null) return currentNode;

        const leftTreeNodes = currentNode.left;
        currentNode.left = currentNode.right;
        currentNode.right = leftTreeNodes;

        traverse(currentNode.left);
        traverse(currentNode.right);

        return currentNode;
    }
    traverse(root.left);

    const leftTreeNodes = root.left;
    const rightTreeNodes = root.right;

    // Same tree Logic is being used but the conditions are different;
    function symmetryTraverse(currentNode1, currentNode2){
        if(currentNode1 === null && currentNode2 !== null){
            return false;
        }
        else if(currentNode1 !== null && currentNode2 === null){
            return false;
        }
        else if(currentNode1 === null && currentNode2 === null){
            return true;
        }

        if(currentNode1.val !== currentNode2.val){
            return false;
        }

        const leftTreeSymmetry = symmetryTraverse(currentNode1.left, currentNode2.left);
        const rightTreeSymmetry = symmetryTraverse(currentNode1.right, currentNode2.right);

        return leftTreeSymmetry && rightTreeSymmetry;
    }
    
    return symmetryTraverse(leftTreeNodes, rightTreeNodes);
};