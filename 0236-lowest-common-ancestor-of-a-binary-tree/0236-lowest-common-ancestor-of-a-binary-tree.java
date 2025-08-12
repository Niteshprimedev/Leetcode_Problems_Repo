/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    TreeNode traverse(TreeNode currNode, TreeNode p, TreeNode q){
        // Base Case:
		if(currNode == null){
			return null;
		}
		
		TreeNode leftNode = traverse(currNode.left, p, q);
		
		TreeNode rightNode = traverse(currNode.right, p, q);
		
		if (currNode == p || currNode == q){
			return currNode;
		}
		else if(leftNode != null && rightNode != null){
			return currNode;
		}
		
		return leftNode == null ? rightNode : leftNode;
	}

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return traverse(root, p, q);
    }
}