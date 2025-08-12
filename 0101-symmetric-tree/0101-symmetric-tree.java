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
    void swapNodes(TreeNode currNode){
		if(currNode != null){
			TreeNode leftSubTree = currNode.left;
			currNode.left = currNode.right;
			currNode.right = leftSubTree;
			
			swapNodes(currNode.left);
			swapNodes(currNode.right);
		}
	}

    boolean traverse(TreeNode leftNode, TreeNode rightNode){
		// 	
		if(leftNode == null && rightNode == null){
			return true;
		}
		if(leftNode != null && rightNode != null && leftNode.val == rightNode.val){
			boolean leftTree = traverse(leftNode.left, rightNode.left);
			boolean rightTree = traverse(leftNode.right, rightNode.right);
			
			if(leftTree && rightTree){
				return true;
			}
			return false;
		}
		else{
			return false;
		}
	}

    public boolean isSymmetric(TreeNode root) {
        if(root == null || (root.left == null && root.right == null)){
			return true;
		}
		
		swapNodes(root.left);
		
		return traverse(root.left, root.right);	
    }
}