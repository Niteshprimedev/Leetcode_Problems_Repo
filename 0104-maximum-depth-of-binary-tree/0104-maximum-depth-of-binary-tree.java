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
    public int maxDepth(TreeNode root) {
        // add your logic here
		if(root == null){
			return 0;
		}
		
		Deque<TreeNode> queue = new ArrayDeque<>();
		
		queue.addLast(root);
		int maxDepth = 0;
		
		while(queue.size() > 0){
			maxDepth += 1;
            // System.out.println(queue.size());
            int levelSize = queue.size();
			
			for(int idx = 0; idx < levelSize; idx++){
				TreeNode currNode = queue.removeFirst();
				
				if(currNode.left != null){
					queue.addLast(currNode.left);
				}
				if(currNode.right != null){
					queue.addLast(currNode.right);
				}
			}
		}
		
		return maxDepth;
    }
}