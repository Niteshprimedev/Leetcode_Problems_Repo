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
    private static int traverse(TreeNode currNode, int[] maxPathSum){
        if(currNode == null){
            return Integer.MIN_VALUE;
        }

        int leftPathSum = traverse(currNode.left, maxPathSum);
        int rightPathSum = traverse(currNode.right, maxPathSum);

        if(leftPathSum < 0){
            leftPathSum = 0;
        }

        if(rightPathSum < 0){
            rightPathSum = 0;
        }

        int newMaxPathSum = leftPathSum + rightPathSum + currNode.val;
        maxPathSum[0] = Math.max(maxPathSum[0], newMaxPathSum);

        return currNode.val + Math.max(leftPathSum, rightPathSum);
    }

    public int maxPathSum(TreeNode root) {
        int[] maxPathSum = {Integer.MIN_VALUE};
        traverse(root, maxPathSum);

        return maxPathSum[0];
    }
}