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
var goodNodes = function(root) {

    // Solution: Using DFS - Depth First Search & Array Filter Approach to filter out the nodes/ array items which are in increasing order;
    // Pseudocode
    // Create a totalGoodNodesCount variable and initialize it to 0
    // Create a nodesStack variable and initialize it to an array with root element
    // Create a parentsGoodNodeStack variable and initialize it to an array with - inifinity element
    // Run a while loop as long as the nodesStack is not empty 
    // Create a currentNode variable and initialize it to the last node in the stack by using pop() method
    // Create a parentGoodNodeValue variable and initialize it to 
    // the last node in the parentsGoodNodeStack by using pop() method
    // Increment the totalGoodNodesCount value by 1 if the currentNode.val is greater than the parentGoodNodeValue
    // Create a maxGoodNodeVal variable and initialize it to have the maximum value
    // by comparing the parentGoodNodeValue & the currentNode.val
    // Move and traverse to the left node in the tree if there's a left node;
    // Push the currentNode.left node value into the nodesStack
    // Push the maxGoodNodeVal variable value into the parentsGoodNodeStack
    // Move and traverse to the riht node in the tree if there's a right node
    // Push the currentNode.right node value into the nodesStack
    // Push the maxGoodNodeVal variable value into the parentsGoodNodeStack 
    // Finally, we will have the total number of good nodes count in the totalGoodNodesCount variable for the given
    // binary tree so will return it

    // Variables & Setup
    let totalGoodNodesCount = 0;

    function dfsTraverseRec(currentNode, goodNodeMaxVal){
        // Base Case;
        if(currentNode === null) return;

        // Increment the totalGoodNodesCount if the currentNode is a good node
        if(currentNode.val >= goodNodeMaxVal){
            totalGoodNodesCount++;
        } 
        // Traverse to the left node
        dfsTraverseRec(currentNode.left, Math.max(goodNodeMaxVal, currentNode.val));
        // Traverse to the right node
        dfsTraverseRec(currentNode.right, Math.max(goodNodeMaxVal, currentNode.val));
    }

    // Kick - off the recursion
    dfsTraverseRec(root, Number.NEGATIVE_INFINITY);
    return totalGoodNodesCount;
};