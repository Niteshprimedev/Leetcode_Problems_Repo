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
    private int traverse(TreeNode root, int currNum){
        if(root == null) return 0;

        currNum = currNum | root.val;

        int leftTree = traverse(root.left, currNum << 1);
        int rightTree = traverse(root.right, currNum << 1);

        if(root.left == null && root.right == null){
        // System.out.println("What? " + root.val + " " + currNum);
            return currNum;
        }

        return leftTree + rightTree;
    }

    public int sumRootToLeaf(TreeNode root) {
        return traverse(root, 0);
    }
}