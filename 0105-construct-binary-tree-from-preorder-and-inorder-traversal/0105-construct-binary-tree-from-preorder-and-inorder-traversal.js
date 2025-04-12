/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
class PreInBinaryTree{
    constructor(){
        this.root = null;
    }

    constructTree(preorder, preStart, preEnd, inStart, inEnd, inHashmap){
        // Base Case:
        // when there's no nodes between preStart & preEnd or inStart & inEnd;
        // thst's actually empty array;
        if(preStart > preEnd || inStart > inEnd){
            return null;
        }

        const nodeVal = preorder[preStart];

        const root = new TreeNode(nodeVal);

        // Getting the root node index from inorder traversal array
        // to determine the left subTree and right subTree;

        const inRoot = inHashmap.get(nodeVal);
        const nodesCount = inRoot - inStart;

        const leftPreEnd = preStart + nodesCount;

        root.left = this.constructTree(preorder, preStart + 1, leftPreEnd, inStart, inRoot - 1, inHashmap);
        root.right = this.constructTree(preorder, leftPreEnd + 1, preEnd, inRoot + 1, inEnd, inHashmap);

        return root;
    }
}
var buildTree = function(preorder, inorder) {
    // Logic:
    // Making use of preorder properties and inorder properties:
    // preorder: Root -> Left -> Right
    // inorder: Left -> Root -> Right
    const inOrderElsHashmap = new Map();

    for(let idxI = 0; idxI < inorder.length; idxI++){
        const nodeEl = inorder[idxI];
        inOrderElsHashmap.set(nodeEl, idxI);
    }

    const constructPreInBiTree = new PreInBinaryTree();

    const root = constructPreInBiTree.constructTree(preorder, 0, preorder.length - 1, 0, inorder.length - 1, inOrderElsHashmap);

    return root;
};