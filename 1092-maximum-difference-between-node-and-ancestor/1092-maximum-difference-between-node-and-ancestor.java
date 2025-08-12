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
    void traverse(TreeNode currNode, int maxVal, int minVal, int[] maxDiff){
        if(currNode != null){
            maxVal = Math.max(maxVal, currNode.val);
            minVal = Math.min(minVal, currNode.val);

            maxDiff[0] = Math.max(maxDiff[0], (maxVal - minVal));

            traverse(currNode.left, maxVal, minVal, maxDiff);
            traverse(currNode.right, maxVal, minVal, maxDiff);
        }
    }
    public int maxAncestorDiff(TreeNode root) {
        int[] maxDiff = {Integer.MIN_VALUE};

        traverse(root, Integer.MIN_VALUE, Integer.MAX_VALUE, maxDiff);
        return maxDiff[0];
    }
}