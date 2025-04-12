/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    // Logic used from Max_PATH_SUM Problem
    // where we return the path sum to its root/parent node
    // Similarly, we are checking the LCA on the currentNode and leftSubTree
    // plus rightSubTree level
    // Three Conditions: The root is the lca which is having the p node on the 
    // leftSubTree and q node on rightSubTree
    // The node is the lca which is having the p or q node on the leftSubTree
    // The node is the lca which is having the p or q node on the rightSubTree

    let lcaNode = null;
    let isPthNodeFound = false;
    let isQthNodeFound = false;

    // If p is null & q exist then return q as LCA
    if(p === null && q !== null){
        lcaNode = q;
        return lcaNode;
    }
    // If q is null & p exist then return p as LCA
    else if(p !== null && q === null){
        lcaNode = p;
        return lcaNode;
    }

    // console.log(lcaNode);

    function traverse(currentNode){
        if(currentNode === null){
            return false;
        }

        if(lcaNode !== null){
            return false;
        }

        // Leaf node condition;
        if(currentNode.left === null && currentNode.right === null){
            // When both the p and q are null;
            if(p === null && q === null){
                lcaNode = currentNode;
                return lcaNode;
            }
        }

        const isNodeOnLeftTree = traverse(currentNode.left);
        const isNodeOnRightTree = traverse(currentNode.right);

        let isNodeCurrentNode  = false;

        if(currentNode === p){
            isPthNodeFound = true;
            isNodeCurrentNode = true;
        }
        if(currentNode === q){
            isQthNodeFound = true;
            isNodeCurrentNode = true;
        }

        const isBothPAndQNodesFound = isPthNodeFound && isQthNodeFound;
        const isNodeOnBothLeftAndRightTree = isNodeOnLeftTree && isNodeOnRightTree;

        // THE COMMON ANCESTOR OF P & Q NODES on the root/parent level
        if (isBothPAndQNodesFound && isNodeOnBothLeftAndRightTree){
            lcaNode = currentNode;
            isPthNodeFound = false;
            isQthNodeFound = false;
        }
        // THE COMMON ANCESTOR OF P & Q NODES is the current Node with having
        // P OR Q Node as its descendant on the Left Sub Tree
        else if(isBothPAndQNodesFound && (isNodeOnLeftTree && isNodeCurrentNode)){
            lcaNode = currentNode;
            isPthNodeFound = false;
            isQthNodeFound = false;
        }
        // THE COMMON ANCESTOR OF P & Q NODES is the current Node with having
        // P OR Q Node as its descendant on the Right Sub Tree
        else if(isBothPAndQNodesFound && (isNodeOnRightTree && isNodeCurrentNode)){
            lcaNode = currentNode;
            isPthNodeFound = false;
            isQthNodeFound = false;
        }

        return isNodeCurrentNode || isNodeOnLeftTree || isNodeOnRightTree;
    }

    traverse(root);

    return lcaNode;
};