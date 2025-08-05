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
    private static void traverse(TreeNode root, List<Integer> inOrderTraversal){
        if(root != null){
            if(root.left != null){
                traverse(root.left, inOrderTraversal);
            }
            inOrderTraversal.add(root.val);
            if(root.right != null){
                traverse(root.right, inOrderTraversal);
            }
        }
	}

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inOrderTraversal = new ArrayList<>();
		traverse(root, inOrderTraversal);
		
		return inOrderTraversal;
    }
}