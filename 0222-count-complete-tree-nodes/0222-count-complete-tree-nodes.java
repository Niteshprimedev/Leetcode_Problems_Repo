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
    private int traverse(TreeNode currNode){
        if(currNode == null){
            return 0;
        }

        int leftCount = traverse(currNode.left);
        int rightCount = traverse(currNode.right);

        return 1 + leftCount + rightCount;
    }
    public int countNodes(TreeNode root) {
        return traverse(root);
    }
}