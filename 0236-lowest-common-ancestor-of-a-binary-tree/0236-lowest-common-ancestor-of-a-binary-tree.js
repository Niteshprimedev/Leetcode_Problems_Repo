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
    let lcaNode = [null];
    let isPthNodeFound = false;
    let iQthNodeFound = false;

    function traverse(currentNode, lcaNode){
        // Base Case:
        if(currentNode === null){
            return false;
        }

        const isNodeOnLeftSubtree = traverse(currentNode.left, lcaNode);
        const isNodeOnRightSubtree = traverse(currentNode.right, lcaNode);

        let isCurrentNodePorQ = false;
        if(currentNode === p){
            isCurrentNodePorQ = true;
        }
        if(currentNode === q){
            isCurrentNodePorQ = true;
        }

        const isBothNodesFound = isNodeOnLeftSubtree && isNodeOnRightSubtree;
        const isLeftNodeAndCurrentNode = isCurrentNodePorQ && isNodeOnLeftSubtree;
        const isRightNodeAndCurrentNode = isCurrentNodePorQ && isNodeOnRightSubtree;

        if(isBothNodesFound){
            lcaNode[0] = currentNode;
            return false;
        }
        else if(isLeftNodeAndCurrentNode|| isRightNodeAndCurrentNode){
            lcaNode[0] = currentNode;
            return false;
        }

        if(currentNode === p || currentNode === q){
            return true;
        }

        return isCurrentNodePorQ || isNodeOnLeftSubtree || isNodeOnRightSubtree;
    }
    traverse(root, lcaNode);

    return lcaNode[0];
};