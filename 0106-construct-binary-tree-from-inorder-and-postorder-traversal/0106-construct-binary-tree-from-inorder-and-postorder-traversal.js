/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
class PosInBinaryTree{
    constructor(){
        this.root = null;
    }

    constructTree(postorder, postStart, postEnd, inStart, inEnd, inHashmap){
        // Base Case:
        // Cause its reverse to preorder so in preorder
        // we check for greater preStart and here we check for smaller postStart
        // So replace preStart with the postEnd && figure out the subTrees using visualization;
        if(postStart < postEnd || inStart > inEnd){
            return null;
        }

        const nodeVal = postorder[postStart];

        const root = new TreeNode(nodeVal);
        // console.log(root)

        const inRoot = inHashmap.get(nodeVal);
        const nodesCount = inRoot - inStart;

        const leftPostStart = postEnd + nodesCount - 1;

        root.left = this.constructTree(postorder, leftPostStart, postEnd, inStart, inRoot - 1, inHashmap);
        root.right = this.constructTree(postorder, postStart - 1, leftPostStart + 1, inRoot + 1, inEnd, inHashmap);

        return root;
    }
}
var buildTree = function(inorder, postorder) {
    // Logic:
    // postorder: Left -> Right -> Root
    // inorder: Left -> Root -> Right

    const inOrderElsHashmap = new Map();

    for(let idxI = 0; idxI < inorder.length; idxI++){
        const nodeEl = inorder[idxI];
        inOrderElsHashmap.set(nodeEl, idxI);
    }

    const constructPosInBiTree = new PosInBinaryTree();
    const root = constructPosInBiTree.constructTree(postorder, postorder.length - 1, 0, 0, inorder.length - 1, inOrderElsHashmap);

    return root;
};