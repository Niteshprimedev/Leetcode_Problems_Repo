/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private void traverse(TreeNode[] prevNode, TreeNode currNode, TreeNode[] firstNode, TreeNode[] secondNode){
        // Base Case:
        if(currNode == null){
            return;
        }

        traverse(prevNode, currNode.left, firstNode, secondNode);

        // Inorder logic here:
        // prevNode's value should always be less than the currNode;

        // if prevNode's val is greater currNode.val then initialize firstNode; 
        // keep firstNode pointer on this node
        if(prevNode[0] != null && prevNode[0].val > currNode.val){
            if(firstNode[0] == null){
                firstNode[0] = prevNode[0];
            }
            secondNode[0] = currNode;
            // System.out.println("Prev" + prevNode.val + "first" + firstNode[0].val + "second" + secondNode[0].val);
        }

        prevNode[0] = currNode;
        traverse(prevNode, currNode.right, firstNode, secondNode);

        return;
    }
    public void recoverTree(TreeNode root) {
        // Intuition: We know that inorder of a BST is sorted
        // So if recursive inorder is not sorted then we need to swap
        // But the Question is which two nodes to swap?
        // Case1: Swapping two nodes that are not adjacent, here the
        // nodes have been swapped at some distance
        // Case2: Swapping two adjacent nodes, here the nodes have been
        // swapped at no distance
        // Handling case 2 is easy as we can use prev & curr => similar to
        // finding the minDistance between nodes
        // But the challenge is all about handling the case 1: here we need
        // three pointers: first for first disturbed order, second for second
        // disturbed order and curr for traversing the tree;

        // Now, why? to swap first and curr always? cause let's see the case 2
        // so in case 2 we don't have the second pointer initialized and therefore
        // we need to swap curr and first, so similarly => first and curr needs to
        // be swapped cause swappiing them makes the BST in its correct order;

        // Edge Case;
        if(root == null) return;

        TreeNode[] prevNode = new TreeNode[] {null};
        TreeNode[] firstNode = new TreeNode[] {null};
        TreeNode[] secondNode = new TreeNode[] {null};

        traverse(prevNode, root, firstNode, secondNode);

        // System.out.println("First" + firstNode[0].val + " second " + secondNode[0].val);

        int temp = firstNode[0].val;
        firstNode[0].val = secondNode[0].val;
        secondNode[0].val = temp;
    }
}